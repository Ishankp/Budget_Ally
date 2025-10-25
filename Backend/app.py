from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import os
from plaid2 import PlaidClient
import json
import uuid
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'budget.db')

# Plaid config (replace with your sandbox keys or use env vars)
PLAID_CLIENT_ID = os.environ.get('PLAID_CLIENT_ID', '68fc90a53089da001f96572c')
PLAID_SECRET = os.environ.get('PLAID_SECRET', 'b6acf18dba24078a0985ba402443b3')
PLAID_ENV = os.environ.get('PLAID_ENV', 'sandbox')

# plaid2 client
plaid_client = PlaidClient(
    {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "environment": PLAID_ENV
    },
    "simple"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class BudgetItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'category': self.category,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(36), unique=True, nullable=True)

    def set_password(self, password: str):
        # simple salted hash (for demo). For production use bcrypt/scrypt/argon2.
        salt = 'budgetally_salt'
        self.password_hash = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

    def check_password(self, password: str) -> bool:
        salt = 'budgetally_salt'
        return self.password_hash == hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

    def generate_token(self):
        self.token = str(uuid.uuid4())
        return self.token


class PlaidToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    access_token = db.Column(db.String(512), nullable=False)

    def to_dict(self):
        return {'user_id': self.user_id, 'access_token': self.access_token}


def create_tables():
    db.create_all()

# Register the create_tables function in a way compatible with multiple Flask versions.
# Newer Flask has `before_serving`, older versions use `before_first_request`.
if hasattr(app, 'before_serving'):
    # register as a callback (before_serving is a decorator on newer Flask)
    app.before_serving(create_tables)
elif hasattr(app, 'before_first_request'):
    app.before_first_request(create_tables)
else:
    # fallback: call within an application context so SQLAlchemy can access app configs
    with app.app_context():
        create_tables()


@app.route('/api/items', methods=['GET'])
def list_items():
    items = BudgetItem.query.all()
    return jsonify([i.to_dict() for i in items])


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = BudgetItem.query.get_or_404(item_id)
    return jsonify(item.to_dict())


@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json() or {}
    name = data.get('name')
    amount = data.get('amount')
    category = data.get('category')
    if not name or amount is None:
        return jsonify({'error': 'name and amount are required'}), 400
    item = BudgetItem(name=name, amount=float(amount), category=category)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = BudgetItem.query.get_or_404(item_id)
    data = request.get_json() or {}
    item.name = data.get('name', item.name)
    if 'amount' in data:
        item.amount = float(data['amount'])
    item.category = data.get('category', item.category)
    db.session.commit()
    return jsonify(item.to_dict())


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = BudgetItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'deleted'}), 200


# ---- Auth endpoints ----
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'username and password required'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'username already exists'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'registered'}), 201


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'username and password required'}), 400
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'invalid credentials'}), 401
    token = user.generate_token()
    db.session.commit()
    return jsonify({'token': token})


def get_user_from_token():
    auth = request.headers.get('Authorization', '')
    if auth.startswith('Bearer '):
        token = auth.split(' ', 1)[1]
        return User.query.filter_by(token=token).first()
    return None


@app.route('/api/hello', methods=['GET'])
def protected_hello():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'message': f'Hello, {user.username}!'}), 200



# ---- Plaid endpoints (plaid2) ----
@app.route('/api/plaid/link_token', methods=['POST'])
def plaid_link_token():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    # plaid2 expects dict arguments
    try:
        response = plaid_client.link_token_create(
            {
                "products": ["auth", "transactions", "balance"],
                "client_name": "Budget Ally",
                "country_codes": ["US"],
                "language": "en",
                "user": {"client_user_id": str(user.id)}
            }
        )
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': 'Could not create link token', 'details': str(e)}), 500


@app.route('/api/plaid/exchange_public_token', methods=['POST'])
def plaid_exchange_public_token():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    data = request.get_json() or {}
    public_token = data.get('public_token')
    if not public_token:
        return jsonify({'error': 'public_token required'}), 400
    try:
        exchange_response = plaid_client.item_public_token_exchange({"public_token": public_token})
        access_token = exchange_response.get('access_token')
        if not access_token:
            return jsonify({'error': 'No access_token returned from Plaid', 'details': exchange_response}), 502
        # Store access_token in a separate PlaidToken table (do not overwrite the user's auth token)
        pt = PlaidToken.query.filter_by(user_id=user.id).first()
        if pt:
            pt.access_token = access_token
        else:
            pt = PlaidToken(user_id=user.id, access_token=access_token)
            db.session.add(pt)
        db.session.commit()
        return jsonify({'message': 'Plaid linked', 'access_token': access_token})
    except Exception as e:
        return jsonify({'error': 'Could not exchange public token', 'details': str(e)}), 500


@app.route('/api/plaid/balance', methods=['GET'])
def plaid_balance():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    pt = PlaidToken.query.filter_by(user_id=user.id).first()
    if not pt or not pt.access_token:
        return jsonify({'error': 'no_plaid_link'}), 400
    try:
        balance_response = plaid_client.accounts_balance_get({"access_token": pt.access_token})
        return jsonify(balance_response)
    except Exception as e:
        return jsonify({'error': 'Could not fetch balances', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


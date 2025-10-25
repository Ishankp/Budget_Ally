from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import os
import json
import uuid
import hashlib

# ...existing code...

# Paginated transactions endpoint (moved below app initialization)

# ...existing code...
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import os
import json
import uuid
import hashlib
import plaid
from plaid.api import plaid_api

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'budget.db')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)





class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(128), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(64), nullable=False)
    subtype = db.Column(db.String(64), nullable=True)
    mask = db.Column(db.String(16), nullable=True)
    official_name = db.Column(db.String(128), nullable=True)
    current_balance = db.Column(db.Float, nullable=True)
    available_balance = db.Column(db.Float, nullable=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(128), unique=True, nullable=False)
    account_id = db.Column(db.String(128), db.ForeignKey('account.account_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(32), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    merchant_name = db.Column(db.String(256), nullable=True)
    category = db.Column(db.String(128), nullable=True)
    pending = db.Column(db.Boolean, nullable=True)
# Endpoint to delete all account and transaction records for the current user
@app.route('/api/cleanup_accounts', methods=['POST'])
def cleanup_accounts():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    Account.query.filter_by(user_id=user.id).delete()
    Transaction.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    return jsonify({'message': 'All account and transaction data deleted for user.'}), 200

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


# Plaid integration removed — PlaidToken model and endpoints deleted per user request


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
    import datetime
    from plaid.model.transactions_get_request import TransactionsGetRequest
    from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
    from plaid.model.accounts_get_request import AccountsGetRequest
    from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
    from plaid.model.products import Products
    from plaid.model.country_code import CountryCode
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

    # Plaid sandbox: fetch 2 months of transactions and save to DB
    try:
        # Use a sandbox public_token for demo
        public_token = 'public-sandbox-8a0b6b6a-xxxx-xxxx-xxxx-xxxxxxxxxxxx'  # Plaid official example token
        exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        exchange_response = client.item_public_token_exchange(exchange_request)
        access_token = exchange_response['access_token']

        # Get accounts
        accounts_request = AccountsGetRequest(access_token=access_token)
        accounts_response = client.accounts_get(accounts_request)
        accounts = accounts_response['accounts']
        for acc in accounts:
            account = Account(
                account_id=acc['account_id'],
                user_id=user.id,
                name=acc.get('name', ''),
                type=acc.get('type', ''),
                subtype=acc.get('subtype', ''),
                mask=acc.get('mask', ''),
                official_name=acc.get('official_name', ''),
                current_balance=acc['balances'].get('current'),
                available_balance=acc['balances'].get('available'),
            )
            db.session.merge(account)
        db.session.commit()

        # Get transactions for last 2 months
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=60)
        tx_request = TransactionsGetRequest(
            access_token=access_token,
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            options=TransactionsGetRequestOptions(count=100)
        )
        tx_response = client.transactions_get(tx_request)
        transactions = tx_response['transactions']
        for tx in transactions:
            transaction = Transaction(
                transaction_id=tx['transaction_id'],
                account_id=tx['account_id'],
                user_id=user.id,
                date=tx['date'],
                amount=tx['amount'],
                name=tx.get('name', ''),
                merchant_name=tx.get('merchant_name', ''),
                category=','.join(tx.get('category', [])),
                pending=tx.get('pending', False)
            )
            db.session.merge(transaction)
        db.session.commit()
    except Exception as e:
        print('Plaid fetch error:', e)

    return jsonify({'token': token})


# Logout endpoint that also triggers cleanup
@app.route('/api/logout', methods=['POST'])
def logout():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    # Remove all account and transaction data for this user
    Account.query.filter_by(user_id=user.id).delete()
    Transaction.query.filter_by(user_id=user.id).delete()
    # Remove token to log out
    user.token = None
    db.session.commit()
    return jsonify({'message': 'Logged out and all account/transaction data deleted.'}), 200


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



# Plaid integration removed — endpoints deleted per user request
client_id='68fc90a53089da001f96572c'
secret = 'b6acf18dba24078a0985ba402443b3'
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


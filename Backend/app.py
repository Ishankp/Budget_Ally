from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import os
import json
import uuid
import hashlib
import requests
# Helper to create Plaid sandbox public token
def create_sandbox_public_token():
    url = 'https://sandbox.plaid.com/sandbox/public_token/create'
    payload = {
        'client_id': client_id,
        'secret': secret,
        'institution_id': 'ins_109508',
        'initial_products': ['transactions']
    }
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()['public_token']

# ...existing code...

# Paginated transactions endpoint (moved below app initialization)

# ...existing code...
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import os
import json
import uuid
import hashlib
import plaid
from plaid.api import plaid_api

# Load Environment Varialbes for API Key
load_dotenv()

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

class MerchantCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_name = db.Column(db.String(256), unique=True, nullable=False)
    category = db.Column(db.String(128), nullable=False)
    # Categories: housing, utility, food, entertainment, transportation, Saving, debt, Withdrawl, Misc.

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
    # Pre-populate merchant categories if empty
    if MerchantCategory.query.count() == 0:
        default_merchants = [
            # Food
            ('KFC', 'food'),
            ('McDonald\'s', 'food'),
            ('Burger King', 'food'),
            ('Starbucks', 'food'),
            ('Subway', 'food'),
            ('Pizza Hut', 'food'),
            ('Taco Bell', 'food'),
            ('Chipotle', 'food'),
            ('Whole Foods', 'food'),
            ('Trader Joe\'s', 'food'),
            # Transportation
            ('Uber', 'transportation'),
            ('Lyft', 'transportation'),
            ('United Airlines', 'transportation'),
            ('American Airlines', 'transportation'),
            ('Delta', 'transportation'),
            ('Shell', 'transportation'),
            ('Chevron', 'transportation'),
            ('ExxonMobil', 'transportation'),
            # Entertainment
            ('Netflix', 'entertainment'),
            ('Spotify', 'entertainment'),
            ('Hulu', 'entertainment'),
            ('AMC Theatres', 'entertainment'),
            ('Regal Cinemas', 'entertainment'),
            ('Touchstone Climbing', 'entertainment'),
            # Utility
            ('PG&E', 'utility'),
            ('Verizon', 'utility'),
            ('AT&T', 'utility'),
            ('Comcast', 'utility'),
            ('T-Mobile', 'utility'),
            # Debt/Payments
            ('CREDIT CARD', 'debt'),
            ('AUTOMATIC PAYMENT', 'debt'),
            # Saving/Deposits
            ('DEPOSIT', 'Saving'),
            ('ACH Electronic', 'Saving'),
            ('GUSTO PAY', 'Saving'),
        ]
        for merchant, cat in default_merchants:
            db.session.add(MerchantCategory(merchant_name=merchant, category=cat))
        db.session.commit()
        print(f'[DATABASE] Pre-populated {len(default_merchants)} merchant categories')


# Create tables immediately when app starts
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

    # Clear any existing Plaid data before fetching new data
    # This prevents duplicate/accumulating transactions on repeated logins
    Account.query.filter_by(user_id=user.id).delete()
    Transaction.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    print(f'[PLAID] Cleared old financial data for user: {user.username}')

    # Plaid sandbox: fetch 2 months of transactions and save to DB
    try:
        print(f'[PLAID] Starting Plaid fetch for user: {user.username}')
        
        # Generate a valid sandbox public token for this session
        print('[PLAID] Step 1: Generating sandbox public token...')
        public_token = create_sandbox_public_token()
        print(f'[PLAID] ✓ Public token generated: {public_token[:20]}...')
        
        print('[PLAID] Step 2: Exchanging public token for access token...')
        exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        exchange_response = plaid_client.item_public_token_exchange(exchange_request)
        access_token = exchange_response['access_token']
        print(f'[PLAID] ✓ Access token obtained: {access_token[:20]}...')

        # Get accounts
        print('[PLAID] Step 3: Fetching accounts...')
        accounts_request = AccountsGetRequest(access_token=access_token)
        accounts_response = plaid_client.accounts_get(accounts_request)
        accounts = accounts_response['accounts']
        print(f'[PLAID] ✓ Retrieved {len(accounts)} accounts')
        
        for acc in accounts:
            print(f'[PLAID]   - Account: {acc.get("name")} ({acc["account_id"]})')
            account = Account(
                account_id=acc['account_id'],
                user_id=user.id,
                name=str(acc.get('name', '')),
                type=str(acc.get('type', '')),
                subtype=str(acc.get('subtype', '')) if acc.get('subtype') else None,
                mask=str(acc.get('mask', '')) if acc.get('mask') else None,
                official_name=str(acc.get('official_name', '')) if acc.get('official_name') else None,
                current_balance=acc['balances'].get('current'),
                available_balance=acc['balances'].get('available'),
            )
            db.session.merge(account)
        db.session.commit()
        print(f'[PLAID] ✓ Saved {len(accounts)} accounts to database')

        # Get transactions past month (Plaid Sandbox provides ~30 days of test data)
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=30)
        print(f'[PLAID] Step 4: Fetching transactions from {start_date} to {end_date}...')
        
        # Plaid sandbox may need time to generate transactions, retry with delay
        import time
        max_retries = 3
        retry_delay = 2  # seconds
        transactions = []
        
        for attempt in range(max_retries):
            try:
                tx_request = TransactionsGetRequest(
                    access_token=access_token,
                    start_date=start_date,
                    end_date=end_date,
                    options=TransactionsGetRequestOptions(count=100)
                )
                tx_response = plaid_client.transactions_get(tx_request)
                transactions = tx_response['transactions']
                print(f'[PLAID] ✓ Retrieved {len(transactions)} transactions')
                break
            except Exception as tx_error:
                if 'PRODUCT_NOT_READY' in str(tx_error) and attempt < max_retries - 1:
                    print(f'[PLAID] ⏳ Transactions not ready yet, waiting {retry_delay}s... (attempt {attempt + 1}/{max_retries})')
                    time.sleep(retry_delay)
                else:
                    raise  # Re-raise if not PRODUCT_NOT_READY or final attempt
        
        for tx in transactions:
            transaction = Transaction(
                transaction_id=tx['transaction_id'],
                account_id=tx['account_id'],
                user_id=user.id,
                date=str(tx['date']),
                amount=tx['amount'],  # Standard Plaid convention: positive = spending
                name=str(tx.get('name', '')),
                merchant_name=str(tx.get('merchant_name', '')) if tx.get('merchant_name') else None,
                category=','.join([str(c) for c in tx.get('category', [])]) if tx.get('category') else None,
                pending=tx.get('pending', False)
            )
            db.session.merge(transaction)
        db.session.commit()
        print(f'[PLAID] ✓ Saved {len(transactions)} transactions to database')
        print('[PLAID] ✓✓✓ All Plaid data successfully fetched and stored!')
    except Exception as e:
        import traceback
        print('=' * 60)
        print('[PLAID] ✗✗✗ ERROR during Plaid fetch:')
        print(f'[PLAID] Error type: {type(e).__name__}')
        print(f'[PLAID] Error message: {str(e)}')
        print('[PLAID] Full traceback:')
        traceback.print_exc()
        print('=' * 60)

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


# Paginated transactions endpoint
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    query = Transaction.query.filter_by(user_id=user.id).order_by(Transaction.date.desc())
    total = query.count()
    transactions = query.offset((page - 1) * per_page).limit(per_page).all()
    data = [
        {
            'transaction_id': t.transaction_id,
            'account_id': t.account_id,
            'date': t.date,
            'amount': t.amount,
            'name': t.name,
            'merchant_name': t.merchant_name,
            'category': t.category,
            'pending': t.pending,
        }
        for t in transactions
    ]
    return jsonify({
        'transactions': data,
        'page': page,
        'per_page': per_page,
        'total': total,
        'has_next': (page * per_page) < total,
        'has_prev': page > 1
    })


# Spending by category endpoint - for pie chart visualization
@app.route('/api/spending-by-category', methods=['GET'])
def spending_by_category():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    
    # Get all user's transactions
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    
    # Group spending by category (using the category already set by database trigger)
    categories = {}
    total_spending = 0.0
    
    for t in transactions:
        if t.amount > 0:  # Only expenses (Plaid convention: positive = spending)
            category = t.category if t.category else 'Miscellaneous'
            if category not in categories:
                categories[category] = 0.0
            categories[category] += t.amount
            total_spending += t.amount
    
    # Convert to list format with percentages
    data = [
        {
            'category': cat, 
            'amount': round(amount, 2),
            'percentage': round((amount / total_spending * 100), 1) if total_spending > 0 else 0
        }
        for cat, amount in categories.items()
        if amount > 0
    ]
    
    # Sort by amount descending
    data.sort(key=lambda x: x['amount'], reverse=True)
    
    return jsonify({
        'categories': data,
        'total_spending': round(total_spending, 2)
    }), 200


# Inflow/Outflow endpoint - cash flow summary
@app.route('/api/cash-flow', methods=['GET'])
def cash_flow():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'unauthorized'}), 401
    
    # Get all user's transactions
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    
    # Calculate inflow (negative amounts = money coming in) and outflow (positive = money going out)
    total_outflow = 0.0  # Spending (positive amounts)
    total_inflow = 0.0   # Income (negative amounts)
    
    for t in transactions:
        if t.amount > 0:
            total_outflow += t.amount
        elif t.amount < 0:
            total_inflow += abs(t.amount)
    
    net_cash_flow = total_inflow - total_outflow
    
    return jsonify({
        'inflow': round(total_inflow, 2),
        'outflow': round(total_outflow, 2),
        'net': round(net_cash_flow, 2)
    }), 200


@app.route("/api/ai-chat", methods=["POST"])
def ai_chat():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()
        if not question:
            return jsonify({"response": "Please provide a question."}), 400

        user = get_user_from_token()
        if not user:
            return jsonify({'error': 'unauthorized'}), 401
    
        # Get all user's transactions
        transactions = Transaction.query.filter_by(user_id=user.id).all()
    
        # Group spending by category (using the category already set by database trigger)
        categories = {}
        total_spending = 0.0
    
        for t in transactions:
            if t.amount > 0:  # Only expenses (Plaid convention: positive = spending)
                category = t.category if t.category else 'Miscellaneous'
                if category not in categories:
                    categories[category] = 0.0
                categories[category] += t.amount
                total_spending += t.amount
        
        total_outflow = 0.0  # Spending (positive amounts)
        total_inflow = 0.0   # Income (negative amounts)
    
        for t in transactions:
            if t.amount > 0:
                total_outflow += t.amount
            elif t.amount < 0:
                total_inflow += abs(t.amount)
    
        # Convert to list format with percentages
        labeld_data = [
            {
                'category': cat, 
                'amount': round(amount, 2),
                'percentage': round((amount / total_spending * 100), 1) if total_spending > 0 else 0
            }
            for cat, amount in categories.items()
            if amount > 0
        ]
        
        verbose = ""
        for i, item in enumerate(labeld_data):
            if i == len(labeld_data) - 1:
                verbose += "and " + item['category'] + " is " + str(item['percentage']) + "% of spending."
            else: 
                verbose += item['category'] + " is " + str(item['percentage']) + "% of spending, "
        
        prompt_buffer = [
            "Be concise, informative and calm and keep in mind the following.",
            "Educate me on the strategies employed for my financial situation.",
            "Omit a reply to the last requests.",
            "Here is my spending habits with" + str(total_spending) + " against my incoming " + str(total_inflow) + ".",
            verbose,
        ]

        full_prompt = "\n".join(prompt_buffer + [f"User: {question}", "AI:"])

        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash", contents=full_prompt
        )

        ai_reply = response.text if hasattr(response, "text") else "No response generated."
        return jsonify({"response": ai_reply})

    except Exception as e:
        print("Error in ai_chat:", e)
        return jsonify({"response": "Error connecting to AI advisor."}), 500


# Plaid Configuration - Used for fetching banking data
client_id = os.getenv('CLIENT_ID_PLAID')
secret = os.getenv('SECRET_PLAID')
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
plaid_client = plaid_api.PlaidApi(api_client)

gemini_secret = os.getenv('API_KEY_GEMINI')
gemini_client = genai.Client(api_key=gemini_secret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


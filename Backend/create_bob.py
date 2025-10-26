import sqlite3
import hashlib

# Database connection
conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

# -----------------------------
# 1. Create Bob's account (user)
# -----------------------------
salt = 'budgetally_salt'
password = 'square'
password_hash = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

cursor.execute("SELECT id FROM user WHERE username = ?", ('Bob',))
bob = cursor.fetchone()

if not bob:
    cursor.execute(
        "INSERT INTO user (username, password_hash) VALUES (?, ?)",
        ('Bob', password_hash)
    )
    conn.commit()
    print("✓ Bob created.")
else:
    print("✓ Bob already exists.")

# Get Bob's user ID
cursor.execute("SELECT id FROM user WHERE username = 'Bob'")
bob_id = cursor.fetchone()[0]

# -----------------------------
# 2. Create Bob's checking account
# -----------------------------
cursor.execute("SELECT account_id FROM account WHERE user_id = ? LIMIT 1", (bob_id,))
account_exists = cursor.fetchone()

if not account_exists:
    cursor.execute(
        """
        INSERT INTO account (account_id, user_id, name, type, subtype, mask, official_name, current_balance, available_balance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            'bob_checking_001',
            bob_id,
            'Bob Checking',
            'checking',
            'personal',
            '1234',
            "Bob's Checking Account",
            0.0,
            0.0
        )
    )
    conn.commit()
    print("✓ Bob's checking account created.")
else:
    print("✓ Bob's account already exists.")

# -----------------------------
# 3. Insert Bob's transactions
# -----------------------------
transactions = [
    # amount, date, name, category
    (-2500.00, '2025-10-01', 'Monthly Paycheck', 'Saving'),
    (-150.00,  '2025-10-15', 'Freelance Project', 'Saving'),
    (1200.00, '2025-10-03', 'Rent Payment', 'debt'),
    (100.00,  '2025-10-04', 'Electric Bill', 'utility'),
    (60.00,   '2025-10-05', 'Water Bill', 'utility'),
    (75.00,   '2025-10-06', 'Internet Bill', 'utility'),
    (45.00,   '2025-10-07', 'Grocery Store', 'food'),
    (38.50,   '2025-10-09', 'Restaurant Dinner', 'food'),
    (12.75,   '2025-10-10', 'Coffee Shop', 'food'),
    (85.90,   '2025-10-12', 'Supermarket', 'food'),
    (28.00,   '2025-10-14', 'Fast Food', 'food'),
    (95.00,   '2025-10-18', 'Weekly Groceries', 'food'),
    (50.00,   '2025-10-08', 'Gas Station', 'transportation'),
    (25.00,   '2025-10-15', 'Uber Ride', 'transportation'),
    (20.00,   '2025-10-17', 'Bus Pass Refill', 'transportation'),
    (35.00,   '2025-10-22', 'Car Wash', 'transportation'),
    (15.00,   '2025-10-11', 'Streaming Subscription', 'entertainment'),
    (22.00,   '2025-10-16', 'Movie Theater', 'entertainment'),
    (40.00,   '2025-10-19', 'Concert Ticket', 'entertainment'),
    (65.00,   '2025-10-13', 'Gym Membership', 'entertainment'),
    (120.00,  '2025-10-20', 'Clothing Store', 'shopping'),
    (30.00,   '2025-10-21', 'Pharmacy', 'shopping'),
    (10.00,   '2025-10-23', 'Donation', 'miscellaneous'),
    (300.00,  '2025-10-25', 'Transfer to Savings', 'Saving'),
    # September transactions
    (-2500.00, '2025-09-26', 'Monthly Paycheck', 'Saving'),
    (1200.00, '2025-09-27', 'Rent Payment', 'debt'),
    (95.00,   '2025-09-28', 'Grocery Store', 'food'),
    (50.00,   '2025-09-29', 'Gas Station', 'transportation'),
    (85.00,   '2025-09-30', 'Utility Bills', 'utility')
]

account_id = 'bob_checking_001'

# Check if transactions already exist
cursor.execute('SELECT COUNT(*) FROM "transaction" WHERE user_id = ?', (bob_id,))
txn_count = cursor.fetchone()[0]

if txn_count == 0:
    for i, (amount, date, name, category) in enumerate(transactions, start=1):
        cursor.execute(
            """
            INSERT INTO "transaction" (
                transaction_id, account_id, user_id, date, amount, name, merchant_name, category, pending
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                f"bob_txn_{i}",
                account_id,
                bob_id,
                date,
                amount,
                name,
                name,  # merchant_name same as name for now
                category,  # category assigned
                False
            )
        )
    conn.commit()
    print(f"✓ {len(transactions)} transactions inserted for Bob.")
else:
    print("✓ Bob's transactions already exist.")

# -----------------------------
# 4. Verify
# -----------------------------
cursor.execute('SELECT COUNT(*) FROM "transaction" WHERE user_id = ?', (bob_id,))
count = cursor.fetchone()[0]
print(f"✓ Bob now has {count} total transactions.")

conn.close()

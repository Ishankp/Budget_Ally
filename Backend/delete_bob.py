import sqlite3

# Database connection
conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

# Delete Bob's transactions
cursor.execute('DELETE FROM "transaction" WHERE user_id IN (SELECT id FROM user WHERE username = "Bob")')
txn_deleted = cursor.rowcount

# Delete Bob's accounts
cursor.execute('DELETE FROM account WHERE user_id IN (SELECT id FROM user WHERE username = "Bob")')
acc_deleted = cursor.rowcount

# Delete Bob's user record
cursor.execute('DELETE FROM user WHERE username = "Bob"')
user_deleted = cursor.rowcount

conn.commit()

print(f"✓ Deleted {txn_deleted} transactions")
print(f"✓ Deleted {acc_deleted} accounts")
print(f"✓ Deleted {user_deleted} user record(s)")
print("✓ Bob and all associated records deleted from database")

conn.close()

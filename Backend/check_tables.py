import sqlite3

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

# Check all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("All tables in database:")
for table in tables:
    print(f"  - {table[0]}")

print("\n" + "=" * 60)

# Check if merchant_category table has data
cursor.execute("SELECT merchant_name, category FROM merchant_category LIMIT 10")
rows = cursor.fetchall()

print("\nMerchant_category table (first 10 rows):")
for merchant, cat in rows:
    print(f"  {merchant:30s} -> {cat}")

conn.close()

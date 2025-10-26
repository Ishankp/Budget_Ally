import sqlite3

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

# Check for triggers
cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='trigger'")
triggers = cursor.fetchall()

print("Database triggers:")
print("=" * 60)
for name, sql in triggers:
    print(f"Trigger: {name}")
    print(sql)
    print("-" * 60)

if not triggers:
    print("No triggers found")

conn.close()

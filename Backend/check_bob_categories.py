import sqlite3

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

cursor.execute('SELECT name, category FROM "transaction" WHERE user_id = (SELECT id FROM user WHERE username = "Bob") ORDER BY date DESC')
rows = cursor.fetchall()

print(f'Bob has {len(rows)} transactions:')
print('-' * 50)
for name, cat in rows[:10]:  # Show first 10
    print(f'{name:30s} -> {cat}')

conn.close()

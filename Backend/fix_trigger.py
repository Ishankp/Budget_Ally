import sqlite3

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

# Drop the old trigger
cursor.execute("DROP TRIGGER IF EXISTS label_transactions")

# Create new trigger with correct table name
cursor.execute("""
CREATE TRIGGER label_transactions
AFTER INSERT ON "transaction"
FOR EACH ROW
BEGIN
    UPDATE "transaction"
    SET category = COALESCE(
        (SELECT category
         FROM merchant_category
         WHERE LOWER(NEW.name) LIKE '%' || LOWER(merchant_name) || '%'
         LIMIT 1),
        'Miscellaneous'
    )
    WHERE id = NEW.id;
END
""")

conn.commit()
print("✓ Trigger updated to use merchant_category table")

conn.close()

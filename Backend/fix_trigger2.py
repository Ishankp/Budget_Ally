import sqlite3

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

# Drop the old trigger
cursor.execute("DROP TRIGGER IF EXISTS label_transactions")

# Create new trigger with EXACT match (case-insensitive)
cursor.execute("""
CREATE TRIGGER label_transactions
AFTER INSERT ON "transaction"
FOR EACH ROW
BEGIN
    UPDATE "transaction"
    SET category = COALESCE(
        (SELECT category
         FROM merchant_category
         WHERE LOWER(merchant_name) = LOWER(NEW.name)
         LIMIT 1),
        NEW.category,
        'Miscellaneous'
    )
    WHERE id = NEW.id;
END
""")

conn.commit()
print("✓ Trigger updated with exact name matching")

conn.close()

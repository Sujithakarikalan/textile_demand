import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
order_id TEXT PRIMARY KEY,
user_id INTEGER NOT NULL,
product_id INTEGER,
product_name TEXT NOT NULL,
quantity INTEGER NOT NULL,
required_fabric REAL NOT NULL DEFAULT 0,
size TEXT NOT NULL DEFAULT 'M',
fabric_received INTEGER NOT NULL DEFAULT 0,
status TEXT NOT NULL,
order_date TEXT NOT NULL,
due_date TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Orders table created successfully")

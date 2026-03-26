import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Delete old users table
cursor.execute("DROP TABLE IF EXISTS users")

# Create correct users table
cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT,
    role TEXT
)
""")

conn.commit()
conn.close()

print("Users table recreated successfully!")
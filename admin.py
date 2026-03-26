import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO users(username,email,password,role)
VALUES('admin','admin@gmail.com','admin123','admin')
""")

conn.commit()
conn.close()
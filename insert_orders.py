import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

orders = [
("ORD-001","Rupa & Co","Innerwear",2500,2500,"In Production","2025-02-10"),
("ORD-002","Arrow Shirts","Formal Shirts",1800,1800,"Completed","2025-01-28"),
("ORD-003","Lilliput Kids","Kidswear",3200,3200,"Quality Check","2025-02-15"),
("ORD-004","Peter England","Casual Shirts",2100,2100,"Dispatched","2025-01-25"),
("ORD-005","Lux Industries","Innerwear",4000,3500,"Awaiting Fabric","2025-02-20"),
("ORD-006","Gini & Jony","Kidswear",1500,1500,"In Production","2025-02-18"),
("ORD-007","Raymond","Formal Shirts",900,900,"Completed","2025-01-30"),
("ORD-008","Jockey","Innerwear",5000,4800,"In Production","2025-02-25")
]

cursor.executemany("""
INSERT INTO orders(order_id,brand,product,quantity,fabric_received,status,due_date)
VALUES(?,?,?,?,?,?,?)
""", orders)

conn.commit()
conn.close()

print("Orders inserted successfully")
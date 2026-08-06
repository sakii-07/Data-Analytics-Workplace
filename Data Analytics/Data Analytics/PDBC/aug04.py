from mysql.connector import connect

conn = connect(
    user = 'root',
    password = 'root',
    port = 3306,
    host = '127.0.0.1',
    database = 'product'
    )

print("Done")

cur = conn.cursor(dictionary=True)
# query = "show databases"

# cur.execute(query)

# for record in cur:
#     print(record[0])

# db = input("Enter database name : ")
# query = f"use {db}"

# cur.execute(query)

# query = "show tables"
# cur.execute(query)
# for i in cur:
#     print(i)

# table = input("Enter table name : ")

# query = f"select * from {table}"
# cur.execute(query)
# for records in cur:
#     print(records)

query = 'select pro_id, name, price from product'
cur.execute(query)
# for record in cur:
#     print(record['price'])

records = cur.fetchall()
print(records)

cur.execute(query)
record1 = cur.fetchone()
print(record1)

record2 = cur.fetchone()
print(record2)
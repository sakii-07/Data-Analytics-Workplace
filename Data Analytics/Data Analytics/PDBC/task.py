from mysql.connector import connect

conn = connect(
    user = 'root',
    password = 'root',
    host = '127.0.0.1',
    port = 3306,
    database = 'oppo_db'
)

cur = conn.cursor(dictionary=True)

# Way - 1
query = 'select model_no, model_name, mrp from mobile where mrp > 20000'
cur.execute(query)
records = cur.fetchall()
for data in records:
    print(data['model_no'],data['model_name'])

# Way -2
query = 'select model_no, model_name, mrp from mobile'
cur.execute(query)
records = cur.fetchall()
for data in records:
    if int(data['mrp']) > 20000:
        print(data['model_no'],data['model_name'])
from mysql.connector import connect

conn = connect(
    user = 'root',
    password = 'root',
    host = '127.0.0.1',
    port = 3306,
    database = 'oppo_db'
)

# cur = conn.cursor()
# model_no = int(input("Enter model no : "))
# model_name = input("Enter model name : ")
# mrp = input("Enter model mrp : ")
# query = f"insert into mobile values({model_no},'{model_name}','{mrp}')"
# cur.execute(query)
# conn.commit()


# data = input("Enter the model_no , model_name and mrp of mobile : ").split()
# print(data)
# query = f"insert into mobile values({data[0]},'{data[1]}','{data[2]}')"
# cur.execute(query)
# conn.commit()

# try:
#     model_no = input("Enter Model number : ")
#     mrp = input("Enter mrp ")

#     query = f"update mobile set mrp = {mrp} where model_no = {model_no}"
#     print("Done")
#     conn.commit()
# except Exception as e:
#     print("Error : ", e)

cur = conn.cursor(dictionary=True)
try:
    query1 = f"create table high_rating(pid int, pname varchar(32))"
    query2 = f"create table low_rating(pid int, pname varchar(32))"
    cur.execute(query1)
    cur.execute(query2)

    query = "select pid, pname, category, mrp, rating from products"
    cur.execute(query)
    data = cur.fetchall()
    for record in data:
        if record['rating']>3:
            query = f"insert into high_rating values({record['pid']},'{record['pname']}')"
            cur.execute(query)
            conn.commit()
        else:
             query = f"insert into low_rating values({record['pid']},'{record['pname']}')"
             cur.execute(query)
             conn.commit()
except Exception as e:
    print("Error : ", e)
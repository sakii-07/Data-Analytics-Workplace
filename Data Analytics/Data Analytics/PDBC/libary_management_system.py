from mysql.connector import connect

conn = connect(
    user = "root",
    password = 'root',
    host = '127.0.0.1',
    port = 3306,
    database = 'library_management_system_db'
)

cu = conn.cursor(dictionary=True)

def CreateTable():
    try:
        t_name = input("Enter Table Name : ").strip()
        num = int(input("Enter number of columns : "))
        col = []
        for _ in range(num):
            column_name = input("Enter column name : ").strip()
            dt = input(f"Enter datatype of column {column_name} : ").strip()
            col.append(f"{column_name} {dt}")

        query = f"create table {t_name} ({(",".join(col))})"
        cu.execute(query)
        print(f"\n{t_name} table created successfully ...")
        print()
    except Exception as e:
        print("Error : ", e)

def AddBook():
    try:
        bid = int(input("Enter book id : "))
        bname = input("Enter book name : ").strip()
        price = float(input("Enter book price : "))
        author = input("Enter book author name : ").strip()
        qnty = int(input("Enter book quantity : "))
        query = f"insert into book values({bid},'{bname}',{price},'{author}',{qnty})"
        cu.execute(query)
        conn.commit()
        print("\nBook added successfully .. ")
        print()
    except Exception as e:
        print("Error : ", e)

def UpdateBookPrice():
    try:
        bname = input("Enter book name : ").strip()
        price = float(input("Enter new price : "))

        query = f"update book set price = {price} where bname = '{bname}'"
        cu.execute(query)
        conn.commit()
        print(f"\n{bname.title()} price {price} updated Succesfully")
        print()
    except Exception as e:
        print("Error : ", e)

def DeleteBook():
    try:
        bid = int(input("Enter book id : "))
        query = f"delete from book where bid = {bid}"
        cu.execute(query)
        conn.commit()
        print(f"\nbook deleted successfully .. ")
        print()
    except Exception as e:
            print("Error : ", e)

def ShowBookById():
    try:
        bid = int(input("Enter book id : "))
        query = f"select bid, bname, price, author, qnty from book where bid = {bid}"
        cu.execute(query)
        data = cu.fetchone()
        print("\nBood ID : ",data['bid'])
        print("Bood Name : ",data['bname'])
        print("Bood Price : ",data['price'])
        print("Bood Author : ",data['author'])
        print("Bood Quantity : ",data['qnty'])
        print()
    except Exception as e:
         print("Error : ", e)

def ShowAllBooks():
    try:
        query = "select bid, bname, price, author, qnty from book"
        cu.execute(query)
        data = cu.fetchall()
        print()
        for record in data:
            print(record)
        print()
    except Exception as e:
             print("Error : ", e)

def Truncatetable():
    try:
        t_name = input("Enter table name : ")
        query = f"truncate table {t_name}"
        cu.execute(query)
        print(f"\n{t_name} table truncated successfully...")
        print()
    except Exception as e:
            print("Error : ", e)

def DropTable():
    try:
        t_name = input("Enter table name : ")
        query = f"drop table {t_name}"
        cu.execute(query)
        print()
        print(f"{t_name} table droped successfully .. ")
        print()
    except Exception as e:
        print("Error : ", e)

def DescribeTable():
    try:
        t_name = input("Enter table name : ")
        query = f"desc table {t_name}"
        cu.execute(query)
        data = cu.fetchall()
        print()
        for i in data:
            print(i)
        print()
    except Exception as e:
        print("Error : ", e)

while True:
    print(f" Library Management System ".center(50,'-'))
    print('''
        1. Create table
        2. Add Book
        3. Update Book Price
        4. Delete Book
        5. Show Book By ID
        6. Show All Books
        7. Truncate Table
        8. Drop Table
        9. Describe Table
        10. Exist
    ''')

    ch = int(input("Enter Your Choice : "))

    if ch == 1:
        CreateTable()
    elif ch == 2:
        AddBook()
    elif ch == 3:
        UpdateBookPrice()
    elif ch == 4:
        DeleteBook()
    elif ch == 5:
        ShowBookById()
    elif ch == 6:
        ShowAllBooks()
    elif ch == 7:
          Truncatetable()  
    elif ch == 8:
        DropTable()
    elif ch == 9:
        DescribeTable()
    elif ch ==10:
        break
    else:
        print("Invalid Choice")
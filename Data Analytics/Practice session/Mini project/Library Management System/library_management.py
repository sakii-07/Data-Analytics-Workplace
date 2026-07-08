import csv
from datetime import datetime

class Member:

    def __init__(self):
        pass

    def create_new_member(self):

        try:
            name = input("Enter name : ")
            email = input("Enter email : ")
            mobile = input("Enter mobile number : ")

            with open('members.csv','r') as file:
                reader = list(csv.reader(file))

            last_id = int(reader[-1][0])
            new_id = last_id + 1

            for data in reader:
                if data[2] == email and data[3] == mobile:
                    print("\nMembar exist already .. ")
                    return

            with open('members.csv','a',newline="") as file1:
                writer = csv.writer(file1)

                writer.writerow([new_id,name,email,mobile,datetime.now()])
            print("\nMember created successfully ...")
        
        except Exception as e:
            print("Error : ", e)

class Book:

    def __init__(self):
        pass

    def add_new_book(self):

        try:
            b_name = input("Enter book name : ")
            auther = input("Enter author name : ")
            price = input("Enter price : ")
            qnty = input("Enter quantity of book : ")

            with open('books.csv','r') as file:
                reader = list(csv.reader(file))

            last_id = int(reader[-1][0])
            new_id = last_id + 1

            for data in reader:
                if data[1] == b_name and data[2] == auther:
                    print("\nBook exist already .. ")
                    return

            with open('books.csv','a',newline="") as file1:
                writer = csv.writer(file1)

                writer.writerow([new_id,b_name,auther,price,qnty])
            print("\nBook added successfully ...")
        
        except Exception as e:
            print("Error : ",e)

    def remove_book(self):
        try:
            b_id = input("Enter the book id : ")
            qnty = int(input("Enter the qnty to remove : "))
            rows = []
            with open('books.csv','r') as file:
                reader = list(csv.reader(file))

            for data in reader:
                if data[0] == b_id:
                   if qnty < int(data[4]):
                        data[4] = int(data[4]) - qnty
                rows.append(data)

            with open('books.csv','w',newline="") as file1:
                writer = csv.writer(file1)

                writer.writerows(rows)
            print("\nBook removed successfully ...")
                             
        except Exception as e:
            print("Error : ",e)

class Library(Member,Book):

    def issue_book(self):
        try:
            m_id = input("Enter member id : ")
            b_id = input("Enter book id : ")
            with open('records.csv') as file:
                reader = list(csv.reader(file))

            rows = []
            found = False
            for data in reader:
                if data[0] == m_id :
                    issue_list = data[1].split('|')
                    issue_list.append(b_id)
                    data[1] = "|".join(issue_list)
                    found = True
                rows.append(data)

            if not found:
                rows.append([m_id,b_id])

            with open('records.csv','w',newline="") as file1:
                writer = csv.writer(file1)

                writer.writerows(rows)
            print("Book issued successfully .. ") 

        except Exception as e:
            print("Error : ", e)   


    def return_book(self):
       
        try:
            m_id = input("Enter member id : ")
            b_id = input("Enter book id : ")
            with open('records.csv') as file:
                reader = list(csv.reader(file))

            rows = []
            found = False
            for data in reader:
                if data[0] == m_id :
                    issue_list = data[1].split('|')

                    if b_id in issue_list:
                        issue_list.remove(b_id)
                        data[1] = "|".join(issue_list)
                        found = True
                    else:
                        print("This book is not issued to this member.")
                        return
                
                rows.append(data)

            if not found:
                print("Membar not found .. ")

            with open('records.csv','w',newline="") as file1:
                writer = csv.writer(file1)

                writer.writerows(rows)
            print("Book removed successfully .. ") 
        
        except Exception as e:
            print("Error : ", e) 

    def show_member_details(self):
        try:
            m_id = input("Enter member id : ")
            with open('members.csv') as file:
                reader = list(csv.reader(file))

            for data in reader:
                if data[0] == m_id:
                    print(f"""
=========== Member details =============
        Member id : {data[0]}
        Name : {data[1]}
        Email : {data[2]}
        Mobile :  {data[3]}             
        Joining Date : {data[4]}
    """)


        except Exception as e:
            print(e)

    def show_book_details(self):
        try:
            b_id = input("Enter book id : ")
            with open('books.csv') as file:
                reader = list(csv.reader(file))

            for data in reader:
                if data[0] == b_id:
                    print(f"""
========= Member details =============
        Book id : {data[0]}
        Name : {data[1]}
        Price : {data[2]}
        Quantity :  {data[3]}  
""")
                

        except Exception as e:
            print(e)

while True:
    print("""
================================================
          Library management system
================================================
        1. Create New Member
        2. Add New Book
        3. Remove Book
        4. Issue Book
        5. Return book
        6. Show Book Details
        7. Show Member Details
        8. Exist
""")
    
    ch = input("Enter your choice : ")
    l = Library()
    if ch == 1:
        l.create_new_member()
    elif ch == 2:
        l.add_new_book()
    elif ch == 3:
        l.remove_book()
    elif ch == 4:
        l.issue_book()
    elif ch == 5:
        l.remove_book()
    elif ch == 6:
        l.show_book_details()
    elif ch == 7:
        l.show_member_details()
    elif ch == 8:
        break
    else:
        print("Invalid choice")

    c = input("Do you want to continue (y/n) : ").lower()
    if c == 'n':
        break
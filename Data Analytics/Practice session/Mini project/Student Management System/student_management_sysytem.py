import csv

def add_student():
    roll = int(input("Enter the roll number : "))
    name = input("Enter the name : ")
    py = int(input("Enter python marks : "))
    sql = int(input("Enter SQl marks : "))
    pb = int(input("Enter PowerBI marks : "))

    with open("students.csv",'a',newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll,name,py,sql,pb])

    print("\nStudent added successfully!")
    print()

def search_student():
    roll = input("Enter the roll number : ")
    with open("students.csv",'r') as file:
        data = csv.reader(file)
        for d in data:
            if d[0] == roll:
                print("\n*****Student Found*****")
                print("Roll Number : ",d[0])
                print("Name : ",d[1])
                print("Python marks : ",d[2])
                print("SQL marks : ",d[3])
                print("PowerBI marks : ",d[4])
                print()

def cal_percentage():
    roll = input("Enter roll number : ")
    with open("students.csv",'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                marks = list(map(float,row[2:]))
                per  = sum(marks)/len(marks)
                return per


def dis_result():
    roll = input("Enter roll number : ")
    with open("students.csv",'r') as file:
        reader = csv.reader(file)
        print("____Result____")
        for row in reader:
            if row[0] == roll:
                per = cal_percentage()
                if per>35:
                    print("\nPass")
                    break
                else:
                    print("\nFail")
                    break
    print()

def cal_average():
    roll = input("Enter roll number : ")
    with open("students.csv",'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                marks = list(map(float,row[2:]))
                avg = sum(marks)/3
                print("\nAverage",avg)
    print()

def display_all():
    with open("students.csv",'r') as file:
        reader = csv.reader(file)
        for data in reader:
            print(data)
    print()

while True:
    print("=" * 35)
    print("     Student Management System")
    print("=" * 35)
    print("1. Add Student")
    print("2. Search Student By Roll Number")
    print("3. Calculate Percentage")
    print("4. Show Result")
    print("5. Calculate Average Marks")
    print("6. Display All Students")
    print("7. Exit")
    print("=" * 35)

    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        per = cal_percentage()
        print(f"\nPercentage : {per:.2f}%")
        print()
    elif choice == 4:
        dis_result()
    elif choice == 5:
        cal_average()
    elif choice == 6:
        display_all()
    elif choice == 7:
        print("Thank You ...!")
        break
    else:
        print("Invalid choice")
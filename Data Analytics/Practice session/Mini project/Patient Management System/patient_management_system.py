import csv

class Patient:
    def __init__(self,p,n,a,g,d,dn,dt,b,s):
        self.patient_id = p 
        self.name = n 
        self.age = a 
        self.gender = g 
        self.disease = d 
        self.doctor_name = dn 
        self.admission_date = dt 
        self.bill_amount = b 
        self.status = s

    @staticmethod
    def add_patient():
        pid = input("Enter patient id : ")
        nm = input("Enter the name : ")
        age = input("Enter patient age : ")
        gender = input("Enter the gender : ")
        die = input("Enter the disease : ")
        dn = input("Enter the doctor_name : ")
        date = input("Enter the admission date : ")
        bill = input("Enter bill amount : ")
        status = input("Enter status : ")

        p = Patient(pid,nm,age,gender,die,dn,date,bill,status)
        with open("patient_data.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([p.patient_id,p.name, p.age, p.gender, p.disease, p.doctor_name,p.admission_date, p.bill_amount,p.status])

        print("Data saves successfully ... ")

    @staticmethod
    def view_all_patients():
        with open("patient_data.csv","r") as file:
            reader = csv.reader(file)

            for data in reader:
                print(data)

    @staticmethod
    def search_patient(pid):
        with open("patient_data.csv","r") as file:
            reader = csv.reader(file)

            for data in reader:
                if data[0]==pid:
                    print(data)
                else:
                    print("Patient not found : ")

    @staticmethod
    def update_patient(pid):
        with open('patient_data.csv','r',newline="") as file:
            reader = csv.reader(file)

            rows = []
            found = False
            for data in reader:
                if data[0] == str(pid):
                    found = True
                    print("Current details : ", data)

                    data[1] = input("Enter the name : ")
                    data[2] = input("Enter the age : ")
                    data[3] = input("Enter the gender : ")
                    data[4] = input("Enter the disease : ")
                    data[5] = input("Enter the doctor name : ")
                    data[6] = input("Enter the admission date : ")
                    data[7] = input("Enter the bill amount : ")
                    data[8] = input("Enter the status : ")

                rows.append(data)

            with open("patient_data.csv",'w',newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            if found:
                print("Patient updated successfully.")
            else:
                print("Patient ID not found.")

    @staticmethod
    def delete_patient(pid):
        with open("patient_data.csv",'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[0] != pid]
            
        with open("patient_data.csv",'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print("Record deleted successfully")

    @staticmethod
    def cal_bill(pid):
        with open("patient_data.csv","r") as file:
            reader = csv.reader(file)

            for data in reader:
                if data[0]==pid:
                    bill = data[7]
                    print(bill)
                    break
            else:
                print("Patient not found ")

    @staticmethod
    def discharge_patient(pid):
        rows = []

        with open("patient_data.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for data in reader:
                if data[0] == str(pid):
                    data[8] = "Discharged"
                    print("Patient discharged successfully.")
                rows.append(data)

        with open("patient_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    @staticmethod
    def count_patient():
        with open("patient_data.csv","r",newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            count = 0
            for rows in reader:
                count += 1
            print("Total patient : ",count)

    @staticmethod
    def show_patient_by_doctor(doctor_name):
        with open("patient_data.csv","r",newline="") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[5]==doctor_name]
            for data in rows:
                print(data)

    @staticmethod
    def show_patient_by_disease(disease):
        with open("patient_data.csv","r",newline="") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[4]==disease]
            for data in rows:
                print(data)

    @staticmethod
    def highest_bill_patient():
        with open("patient_data.csv",'r',newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  

            max_bill = 0
            highest_patient = None

            for data in reader:
                if int(data[7]) > max_bill:
                    max_bill = int(data[7])
                    highest_patient = data

            if highest_patient:
                print("\nPatient With Highest Bill")
                print("Patient ID :", highest_patient[0])
                print("Name       :", highest_patient[1])
                print("Age        :", highest_patient[2])
                print("Gender     :", highest_patient[3])
                print("Disease    :", highest_patient[4])
                print("Doctor     :", highest_patient[5])
                print("Room No    :", highest_patient[6])
                print("Bill Amount:", highest_patient[7])
            else:
                print("No patient records found.")
               

    @staticmethod
    def average_bill():
        with open("patient_data.csv","r",newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            bill = 0
            count = 0
            for data in reader:
                bill = bill + int(data[7])
                count += 1
            if count > 0:
                print("Average Bill:", bill / count)
            else:
                print("No patient records found.")
    

while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Calculate Bill")
    print("7. Discharge Patient")
    print("8. Count Patients")
    print("9. Show Patients By Doctor")
    print("10. Show Patients By Disease")
    print("11. Highest Bill Patient")
    print("12. Average Bill")
    print("13. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        Patient.add_patient()

    elif choice == 2:
        Patient.view_all_patients()

    elif choice == 3:
        patient_id = input("Enter Patient ID: ")
        Patient.search_patient(patient_id)

    elif choice == 4:
        patient_id = input("Enter Patient ID: ")
        Patient.update_patient(patient_id)

    elif choice == 5:
        patient_id = input("Enter Patient ID: ")
        Patient.delete_patient(patient_id)

    elif choice == 6:
        patient_id = input("Enter Patient ID: ")
        Patient.cal_bill(patient_id)

    elif choice == 7:
        patient_id = input("Enter Patient ID: ")
        Patient.discharge_patient(patient_id)

    elif choice == 8:
        Patient.count_patient()

    elif choice == 9:
        doctor_name = input("Enter Doctor Name: ")
        Patient.show_patient_by_doctor(doctor_name)

    elif choice == 10:
        disease = input("Enter Disease Name: ")
        Patient.show_patient_by_disease(disease)

    elif choice == 11:
        Patient.highest_bill_patient()

    elif choice == 12:
        Patient.average_bill()

    elif choice == 13:
        print("Thank You! Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")
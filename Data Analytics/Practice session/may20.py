# '''
# A compnay stores employee id's every time an employee enter the office.
# some employees scan multiple times. Find unique employee id's.
# '''
# attendance = []
# while True:
#     ch = input("Enter choice to continue : y or n ")
#     if ch.lower() == 'y':
#         eid = int(input("Enter the Employee id : "))

#         attendance.append(eid)
#     else:
#         unique_attendance = set(attendance)
#         # print(unique_attendance)
#         break
# print(f"Employee day login : {attendance}")
# print(f"Employee day unique login : {unique_attendance}")

# way - 2 (without set)
attendance = []
unique_attendance = []

while True:
    ch = input("Enter your choice (y/n) : ")
    if ch.lower() == 'y':
        eid = int(input("Enter the employee id : "))
        attendance.append(eid)
    else:
        for i in attendance:
            if i not in unique_attendance:
                unique_attendance.append(i)

        break

print(f"Employee day login : {attendance}")
print(f"Employee day unique login : {unique_attendance}")

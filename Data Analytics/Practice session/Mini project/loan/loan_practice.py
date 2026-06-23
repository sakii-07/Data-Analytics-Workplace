import csv

def read_file():
    try:
        with open('loan_data.csv','r',newline="") as file:
            reader = csv.reader(file)
            for i in reader:
                print(i)
    except Exception as e:
        print(e)


# with open('loan_data.csv','r') as file:
#     reader = csv.reader(file)

#     for i in reader:
#         if i[3] == 'Graduate':
#             print(i)

# with open('loan_data.csv','r') as file:
#     reader = csv.reader(file)
#     # next(reader,None)
#     for i in reader:
#         if i[6] == 'Business' and int(i[5]) >= 700:
#             print(i)

# with open('loan_data.csv','r') as file:
#     reader = csv.reader(file)
#     # next(reader,None)
#     for i in reader:
#         if i[6] == 'Business' and int(i[5]) >= 700:
#             print(i)

## Calculate simple interest
# with open('loan_data.csv','r') as file:
#     reader = csv.reader(file)
#     all_data = list(reader)
#     for row in all_data[1:]:
#         p = int(row[7])
#         r = float(row[8])
#         y = int(row[9])

#         si = (p*r*y)/100

#         print(f"{row[0]} - {row[1]} - {si}")

## count of default_loan - yes
# with open('loan_data.csv','r') as file:
#     reader = csv.reader(file)
#     all_data = list(reader)
#     count = 0
#     for row in all_data[1:]:
#         if row[-1] == 'Yes':
#             count += 1

#     print(count)

## how many percent customers are default
with open('loan_data.csv','r') as file:
    reader = csv.reader(file)
    all_data = list(reader)
    count = 0
    for row in all_data[1:]:
        if row[-1] == 'Yes':
            count += 1

    print(f"{(count/len(all_data[1:]))*100:0.2f}%")
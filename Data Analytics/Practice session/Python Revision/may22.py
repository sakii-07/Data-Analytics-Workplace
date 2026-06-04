# '''
# Cab booking System
# senario : Find nearrest cab
# '''

# cabs = {"cab1": 2, "cab2":1.4,"cab3":4,"cab4":10,"cab5":0.5,"cab6":2.7}

# nearest_cab = ""
# minimum_distance = 10
# user_location = 5

# for cab,location in cabs.items():
#     d = abs(user_location-location)

#     if d < minimum_distance:
#         minimum_distance = d
#         nearest_cab = cab
# print(f"Neatest cab is -{nearest_cab} with distance {minimum_distance} km")

# Way -2 using list
cab_distance = [10, 3, 8, 2.4, 7.5, 9, 6.1, 3.1,11]

min_distance = cab_distance[0]
my_location = float(input("Enter the your location : "))
min_cab_distance = cab_distance[0]

for i in cab_distance:
    d = abs(my_location-i)

    if d<min_distance:
        min_distance = d
        min_cab_distance = i

print(min_cab_distance)

# '''
# Socail media trending hashtags
# senario : Find the top occuring hashtag
# '''

# hashtag = ["#shivajimaharaj","#modi","#shivajimaharaj","#rohitsharma","#viratkohli","#shivajimaharaj","#rohitsharma","#shivajimaharaj"]

# h_occurances = {}
# max_occurance = {}
# for ht in hashtag:
#     if ht not in h_occurances:
#         h_occurances[ht] = 1
#     else:
#         h_occurances[ht] += 1

# for k,v in h_occurances.items():
#     if h_occurances[k] == max(h_occurances.values()):
#         print(k," : ",v)

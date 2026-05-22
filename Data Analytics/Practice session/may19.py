# even index -- key, odd index -- value

lst = ["name", "Sakshi", "age", 21, "city", "Pune"]

d = {}

for i in range(0, len(lst), 2):
    d[lst[i]] = lst[i+1]

print(d)

# zip function
d = dict(zip(lst[::2], lst[1::2]))
print(d)
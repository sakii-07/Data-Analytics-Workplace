'''
Find student who scored above average marks
'''
stud_marks = {"Sakshi":40,"Sojar":50,"Pranjali":60,"Shital":70}
avg_marks = {}
avg = sum(stud_marks.values())/len(stud_marks)
# avg = sum/len(stud_marks)
for k,v in stud_marks.items():
    if stud_marks[k] >= avg:
        avg_marks[k] = v
print(avg_marks)
        
import numpy as np

salary = [10000,20000,30000,40000,50000]
sal = np.array(salary)
print(np.mean(sal)) # 30000.0

salary = [10000,20000,30000,40000,50000,400000]
sal = np.array(salary)
print(np.mean(sal)) # 91666

salary = [10000,20000,30000,40000,50000,300000,20000]
sal = np.array(salary)
print(np.median(sal)) # 30000.0

# variance 
print(np.var(sal)) # 200000000.0

# Example
marks1 = [71,73,74,75,77]
marks2 = [30,71,73,74,75,77,99]
print(np.var(marks1)) # 4.0
print(np.var(marks2)) # 361.34693877551024

# standard deviantion
print(np.std(marks1)) # 2.0
print(np.std(marks2)) # 19.009127775242877
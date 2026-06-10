import numpy as np

# IQR -- inter quartile range 
#        IQR = Q3-Q1
#   Q1 = 25%, Q2 = 50%, Q3 = 75%

'''
LV = Q1 - 1.5 * IQR
UV = Q3 + 1.5 * IQR
'''
marks = [2,10,13,15,81,83,84,85,86,120,125,397]
mk = np.array(marks)
q1 = np.percentile(mk, 25)
print(q1)

q3 = np.percentile(mk,75)
print(q3)

IQR = q3-q1
print(IQR)

LV = q1 - 1.5 * IQR
UV = q3 + 1.5 * IQR
print(LV)
print(UV)

outlier = [num for num in marks if LV>num or UV<num]
print(outlier)

import matplotlib.pyplot as plt
salary = [7000,40000,42000,45000,46000,48000,100000]
plt.boxplot(salary)
plt.show()


# Skewness
import numpy as np
marks = [71,72,73,74,75]
print(np.mean(marks)) # 73.0
print(np.median(marks)) # 73.0

import numpy as np
marks = [71,72,73,74,75,99]
print(np.mean(marks)) # 77.34
print(np.median(marks)) # 73.5

import numpy as np
marks = [10,71,72,73,74,75]
print(np.mean(marks)) # 62.5
print(np.median(marks)) # 72.5

from scipy import stats 
print(stats.skew(marks))

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(marks,kde=True)
plt.show()
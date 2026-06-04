'''
generate the series : 1 10 100 1000
'''

# n = int(input("Enter the number : "))
# num = 1
# for i in range(1,n+1):
#     print(num, end=" ")
#     num *= 10

'''
0 1 1 2 3 4 8 13 21
'''
# a = 0
# b = 1
# for  i in range(2,n+1):
#     print(a, end = " ")
#     c = a+b
#     a,b = b,c

'''
1 2 3 4 5 4 3 2 1
'''
# n = 5
# val = 1
# step = 1
# for i in range(9):
#     print(val, end=" ")

#     if val == n:
#         step = -1
    
#     val += step

# n = 5
# val = 1
# step = 1
# for i in range(9):
#     print(val, end=" ")

#     if val == n:
#         step = -1

#     val += step

'''
1 11 111 1111
'''
# for i in range(1,n+1):
#     print(10**i//9)

'''
1 10 100 1000 100 10 1
'''
# n = 4
# val = 1
# step = 1
# for i in range(1,8):
#     print(val,end=" ")

#     if val == 10**(n-1):
#         step = -1

#     if step == 1:
#         val *= 10
#     else:
#         val = val/ 10

#     val = int(val)

# '''
# 1 10 100 1000
# '''
# n = int(input())
# num = 1
# for i in range(1,n+1):
#     print(num,end=" ")

#     num *= 10

# '''
# 1 11 111 1111 
# '''
# # n = int(input())
# for i in range(1,int(input())+1):
#     print(10**i//9)

# '''
# 1 2 3 4 5 4 3 2 1
# '''
# n = 5
# val = 1
# step = 1
# for i in range(9):
#     print(val, end=" ")

#     if val == n:
#         step = -1

#     val += step

'''
1 10 100 1000 100 10 1
'''
n = 4
val = 1
step = 1
for i in range(7):
    print(val,end=" ")

    if val == 10**(n-1):
        step = -1

    if step == 1:
        val *= 10
    else:
        val /= 10
    
    val = int(val)
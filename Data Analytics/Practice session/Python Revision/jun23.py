# WAP to cal GCD

def gcd(num1,num2):
    common = 0
    minimun = min(num1,num2)
    for i in range(1,minimun):
        if num1%i == 0 and num2%i == 0:
            common = i
    return common

print(gcd(12,8))

# WAP to cal LCM

def lcm(num1, num2):
    minimum = min(num1,num2)
    maximum = max(num1,num2)
    lcm_value = maximum

    while True:
        if lcm_value%minimum==0:
            return lcm_value
        else:
            lcm_value += maximum

print(lcm(12,8))
"""
def calculate_exp(exp):
    total=0
    for i in exp:
        total=total+i
    return total
    

tom=[1000, 2000, 3000]
joy=[2000, 4000, 6000]

tom_exp=calculate_exp(tom)
joy_exp=calculate_exp(joy)

print("Tom's total expences is: ", tom_exp)
print("joy's total expences is: ", joy_exp)
"""
def sum(a,b):
    total=a+b
    return total
a=int(input("Please enter the 1st number : "))
b=int(input("Please enter the 2st number : "))

n=sum(a,b)
print("sum of two numbers is : ", n)
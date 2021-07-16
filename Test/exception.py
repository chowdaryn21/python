x=input("Enter number1 : ")
y=input("Enter number2 : ")

try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print('Division by Zero exception: ')
    z = None
except TypeError as e:
    print('type error exception')
    z = None
print("Division is :", z)
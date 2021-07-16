"""
exp = [2500, 3300, 6700, 9000]
total = 0

for item in exp:
    total = total + item
print(total)

for i in range(1,11):
    print(i)

for i in range(len(exp)):
    print("Month: ", i +1 , "Expences: ", exp[i])
    total = total + exp[i]
print(total)

key_location="garden"
locations=["garage", "garden", "chair", "Car"]

for i in locations:
    if i == key_location:
        print("key is found in ", i)
        break
    else:
        print("key is not found in ", i)

for i in range(1,6):
    if i%2!=0:
        continue
    print(i*i)
""" 
i=1
while i<=5:
    print(i)
    i = i + 1
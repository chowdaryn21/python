d={"tom":12345, "joy":23456, "jone":345678}
print(d)
d["sam"]=98765
print(d)
print(d["sam"])
del d["sam"]
print(d)

for k,v in d.items():
    print("Key: ",k,"Value:",v)

print("Is tom in d ?", "toms" in d )
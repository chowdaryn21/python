import json
book = {}
book['tom'] = {
    'name': 'tom',
    'address': '203 Spring Valley',
    'phone': '12345' 
}
book['naresh'] = {
    'name': 'naresh',
    'address': '2032 Spring Valley',
    'phone': '123456'
}

s=json.dumps(book)
print(s)
with open("C://Users//chowd//OneDrive//Desktop//jsion.txt", "w") as f:
    f.write(s)
    f.close
r=open("C://Users//chowd//OneDrive//Desktop//jsion.txt", "r")
t=r.read()

print(t)
r.close
books=json.loads(t)
print(books)
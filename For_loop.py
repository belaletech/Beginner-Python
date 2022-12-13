for x in range(5,10):
    print(x)

str="Easy"

for y in str:
    print(y)

student =["belal","ayan","ahan"]
for z in student:
    print(z)

no=int(input("Enter any number :"))
print("Table of",no,"is given below")
for i in range(1,11):
    print(i*no)

friend=["Ambisha","Rinkal","Mahima"]
for name in friend:
    if name=="Rinkal":
        break
    else:
        print(name)
else:
    print("This is else block")

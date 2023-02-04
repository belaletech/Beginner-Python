import math
a=int(input("Enter the value of A\n"))
b=int(input("Enter the value of B\n"))
c=int(input("Enter the value of C\n"))
s=(a+b+c)/2
area=math.sqrt((s*((s-a)*(s-b)*(s-c))))
print(area)
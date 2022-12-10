Principal=float(input("enter Principle :"))
Rate =float(input("Enter Rate "))
Time =float(input("Enter Time (n years) :"))
Simple_Intrest =(Principal*Rate*Time)/100
Amount =Principal*(pow((1+Rate/100),Time))
Compound_Intrest=Amount-Principal
print("Simple Intrest :",Simple_Intrest)
print("Compound Interest :",Compound_Intrest)
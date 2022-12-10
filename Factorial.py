no=int (input("Enter your number = "))
fact=1
for i in range(1,no+1):
    fact=fact*i
    print("Factorial of {} is {}".format(no,fact))
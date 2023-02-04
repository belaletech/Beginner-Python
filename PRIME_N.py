lower = int(input("Enter the lower Interval value: "))
upper = int(input("Enter the upper Interval value: "))
print("your prime number is given below")

#loop through the Interval and check individually
for num in range(lower, upper+1):


    #Number should not be divisible
    #by any number between 1-num
    for x in range(2,num):
        if num%x==0:
            break
    else:
        print(num)
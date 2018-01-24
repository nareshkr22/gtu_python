#Print sum of all numbers within given range

num1 = int(input("Enter the Starting value : "))
num2 = int(input("Enter the Ending value   : "))
total = 0

if num1 > num2:
    print("Starting number cannot be greater")
    exit()
else:
    for i in range(num1 , num2+1):
        total= total + i
        
print("The sum of range({0},{1}) is {2}".format(num1,num2,total))     

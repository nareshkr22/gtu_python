#Print all prime numbers within given range

num1 = int(input("Enter the Starting value : "))
num2 = int(input("Enter the Ending value   : "))

if num1 > num2:
    print("Starting number cannot be greater")
    exit()
else:
    for i in range(num1 , num2+1):
        prime = 1 
        for j in range(2,i):
            if (i % j) == 0:                
                prime = 0
        if prime ==1:
            print(i)
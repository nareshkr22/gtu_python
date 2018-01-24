#print base and power from entered number. If no possibility then display suitable message

num = int(input("Enter a number : "))

    
for i in range(3,8):
    temp = num 
    count = 0
    while temp % i == 0:
        temp = temp / i 
        count = count + 1 
    if temp == 1 and count != 0:
        print("{0} is equal to {1} power {2}".format(num,i,count))
    else:
        print("{0} doesnt have any powers of {1}".format(num,i))
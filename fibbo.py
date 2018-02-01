#Print series of fibonacci numbers upto a given limit using recursion 

def fibbo(num):
    if num <= 1:
        return num
    else:
        return fibbo(num-1) + fibbo(num-2)
    
num = int(input("Enter the number/limit : "))

print("Fibbonaci Series upto {0}".format(num))
a = 1
b = 2 

for i in range(num):
     print(fibbo(i))



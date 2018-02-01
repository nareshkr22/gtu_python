#Print series of fibonacci numbers upto a given limit using recursion 

def fibbo(last,slast,num):
    i = last + slast  
   
    if i <= num:
        print(i)
        fibbo(i, last,num);

      

  
num = int(input("Enter the number/limit : "))

print("Fibbonaci Series upto {0}".format(num))
a = 1
b = 2 
print(1)
print(1)
fibbo(1, 1, num)



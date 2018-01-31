#Write a function that demonstrate use of positional parameters , keyword parameters and default parameters

def pw(a,b):
    mul = 1 
    for i in range(0,b):
        mul = mul * a       
    return mul

num1 = int(raw_input("Enter Number 1 : "))
num2 = int(raw_input("Enter Number 2 :"))


result = pw(num1,num2)  # positional parameter
print("{0} power {1} is {2} ".format(num1,num2,result))
result = pw(a=2,b=2)   # keyword parameter
print("2 power 2 is {0} ".format(result))
result = pw(3,4)  # default parameter
print("3 power 4 is {0} ".format(result))
 
 
        
        
         
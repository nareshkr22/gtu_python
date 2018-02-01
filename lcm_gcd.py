#Print LCM and GCD of 2 numbers using recursion


def gcd(a,b):
    if b <= 0:        
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b,l):
    if l%a == 0 and l%b==0:
        return l
    else:
        l = l+1
        return lcm(a,b,l)
    
    
    
    
    
    
num1= int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
n = gcd(num1,num2)
print(n)
n = lcm(num1,num2,1)
print(n)

#Print binary equivalent of given decimal number using recursion



def d2b(num):
    if num >= 1:
        ele = num % 2        
        d2b(num//2)
        print(ele, end="")
num = int(input("Enter a decimal number"))

d2b(num)
#Check a given string is palindrome or not


def palindrome(str):
    for i in range(0,len(str)):
        t = len(str) - i - 1
        if str[i] == str[t]: 
            return True
        else:
            return False
            
            
            
str = input("Enter the string : ")
flag = palindrome(str.lower())
if flag:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
#Reverse a given string using recursion

def reverse(str,r_str):
    if len(str) <= 0 :    
        return r_str    
    else:
        r_str =  r_str + str[-1]   
        str = str[0:-1]     
        return reverse(str,r_str)
       


str = input("Enter the string : ")
r_str = "" 
reverse_str = reverse(str,r_str) 
print("Reverse of the string {0} is {1}".format(str,reverse_str))
        
   
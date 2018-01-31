#Print sum of all decimal numbers from string of numbers separated by comma

input_str = input("Enter the string of numbers")
total = 0
i= 0 
s=""
for i in range(0,len(input_str)):
 
    if input_str[i] == ',': 
       total = total + float(s)
       s=""
    else:
        s = s + input_str[i]

    i = i+1

total = float(s)  + total 
print("Sum of all the decimal numbers in {0} is {1}".format(input_str,total))

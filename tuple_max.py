#Write and call a function that takes a tuple as an argument and returns max and min number by single return




def take_in(size):
    data_tup = list()
    
    for i in range(0,size):
        num1 = int(input("Enter Number {0} : ".format(i+1)))
        data_tup.append(num1)
    
    return tuple(data_tup)

def max_min(data):
    max = 0
    min = data[0]
    for i in data:
        if i > max:
            max = i
        if i < min:
            min = i
    return (max,min)
    
    
    
size = int(input("How many numbers you want to enter : "))
data = take_in(size)
ma_mi = max_min(data)

print("The Data enter by user is : {0}".format(data))
print("Maximum number is  : {0}".format(ma_mi[0]))
print("Minimum number is  : {0}".format(ma_mi[1]))
    
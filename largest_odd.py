#Print largest odd number from 10 entered numbers

num_list = list()
for i in range(1,11):
    num = int(input("Enter a number "))
    num_list.append(num)

largest = 0 

for number in num_list:
    if number % 2 != 0 and  number > largest:
        largest = number 
        

print largest
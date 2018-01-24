#Print the largest of three numbers entered

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))




if num1 >= num2 and num1 >= num3:
	largest = num1
elif num2>=num1 and num2>=num3:
	largest = num2
else:
	largest = num3


print("The largest number among {0} , {1} , {2}  is {3}".format(num1,num2,num3,largest))
	

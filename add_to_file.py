#A program to read string from user and append it in a file 


fd = open("data.txt","a")


data = input("Enter a string to add into the file : ")

fd.write("Data in append {0} \n".format(data))
fd.close()
exit();
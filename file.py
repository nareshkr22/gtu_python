#A program to read content of file


fd = open("data.txt","r")

content_read = fd.read()
fd.seek(0)
content_readline = fd.readline()
fd.seek(0)
content_readlines = fd.readlines()
fd.seek(0)

print("Content of file is using read() : \n {0}".format(content_read))
print("---------------------------------------------------------------")
print("Content of file is using readline() : \n {0}".format(content_readline))
print("---------------------------------------------------------------")
print("Content of file is using readlines() : \n {0}".format(content_readlines))


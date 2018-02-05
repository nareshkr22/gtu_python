#Program to copy content of one file into another file


fd = open("data.txt","r")
fd1 = open("copy_data.txt","w")

content_read = fd.read()
fd1.write(content_read)
fd.close()
fd1.close()
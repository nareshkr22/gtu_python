#Program to append content of a text file into another

fd = open("data.txt","r")
fd1 = open("append_data.txt","a")

content_read = fd.read()
fd1.write(content_read)
fd.close()
fd1.close()
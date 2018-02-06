#Program to read content of file in reverse order


fd = open("data.txt","rb")

content  = fd.read()
lent = len(content)
ctr = 0
cn = ""
for i in range(0,lent+1):
    fd.seek(-i,2)    
    a = fd.read()
    if len(a) > 0:        
        text = a.decode('utf-8')        
        cn = cn + text[0]

print(cn)

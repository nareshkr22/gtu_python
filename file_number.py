#Program to read a text file and print all numbers present in it 
from _codecs import ascii_decode


fd = open("data.txt","r")

content_read = fd.read()

for i in content_read:
    if ord(i) in range(48,58):
        print(i,end='  ')

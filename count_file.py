#A program to count no. of words, no. of lines, occurrence of particular word, occurrence of particular character, no. of blank spaces in given text file.

fd = open("data.txt","r")

def count_words(fd):
    content = fd.read()
    count = len(content.split())    
    return count
    
def count_lines(fd):
    content = fd.readlines()      
    return len(content)

def blank_space(fd):
    content = fd.read()    
    count = 0
    for i in content:
        if i == ' ':
            count = count + 1
  
    return count  

def occur_word(fd,word):
    content = fd.read()
    count = 0
    data = content.split()
    for i in data:
        if i == word:
            count = count + 1
    return count

def occur_char(fd,char):
    content = fd.read()
    count = 0
    for i in content:
        if i == char:
            count = count + 1
    return count

print('--------------------------------------------------------------------------------')
print("Content of the file : \n{0}".format(fd.read()))
fd.seek(0)
print('--------------------------------------------------------------------------------')
print("Total words in the file  : {0}".format(count_words(fd)))
fd.seek(0)
print('--------------------------------------------------------------------------------')
print("Total lines in the file  : {0}".format(count_lines(fd)))
fd.seek(0)
print('--------------------------------------------------------------------------------')
print("Total blank space in the file  : {0}".format(blank_space(fd)))
fd.seek(0)
print('--------------------------------------------------------------------------------')
inp = input("Enter a word to search in file : ")
print("Total occurrence of word {0} space in the file  : {1}".format(inp,occur_word(fd,inp)))
fd.seek(0)
print('--------------------------------------------------------------------------------')
inp = input("Enter a char to search in file : ")
print("Total occurrence of char {0} space in the file  : {1}".format(inp,occur_char(fd,inp)))
print('--------------------------------------------------------------------------------')   
fd.close() 
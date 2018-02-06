#Program to read a file and capitalize first letter of every word in file


fd = open("data.txt","r")

input = fd.readlines()

fd1 = open("data.txt","w")

capitalized_words = []
for line in input:
    capitalized_words =list()
    words = line.split(' ')
    for word in words:         
        title_case_word = word[0].upper() + word[1:]
        capitalized_words.append(title_case_word)
       
    output = ' '.join(capitalized_words)
    fd1.write(output)
        

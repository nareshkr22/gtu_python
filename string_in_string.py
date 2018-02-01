#Write a function that accepts 2 strings as arguments and returns TRUE if either string occurs anywhere in other

word1 = input('Enter String : ')
word2 = input('Enter String : ')

if(len(word1) < len(word2)):
    temp = word2 
    word2 = word1
    word1 = temp

    

flag = ""
for i in range(0, len(word1)):
    if(word1[i] == word2[0]):        
        for j in range(0, len(word2)):
            if( len(word1) > i+j and word1[i+j] == word2[j]):
                flag = "true"
            else:
                flag = "false"
                    
                
    if(flag == "true"):
        print("String is Exist in other String")
        exit()
    
print("String is Not Exist in other String")
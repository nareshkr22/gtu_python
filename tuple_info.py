#An interactive program which first asks user to enter basic information of at least 10 students and returns required information from information repository

def add_data():
    info_repo = list()
    for i in range(2):
        data = list()
        print("=======Student {0}=======".format(i+1))
        enroll = int(input("Enter Id : "))
        name = input("Enter name : ")
        email = input("Enter email id : ")
        degree = input("Enter Degree : ")
        data.append(enroll)
        data.append(name)
        data.append(email)
        data.append(degree)
        
        info_repo.append(data)
   
    return tuple(info_repo)

def print_data(data):    
    count = 1
    for i in data:
        print("=======Student {0}=======".format(count))
        print("Id : {0}".format(i[0]))
        print("Name : {0}".format(i[1]))
        print("Email : {0}".format(i[2]))
        print("Degree : {0}".format(i[3]))
        count = count + 1
                     
            
           
data = add_data()

print_data(data)
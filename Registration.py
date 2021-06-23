def enter_username():
    username = input("Enter your name: ")
    return username
    
def enter_password():
    password = input("Enter your password: ")
    return password

def login(username, password):
    success = False
    file = open("user_data.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == username and b == password):
            success = True
            break

    file.close()

    if (success):
        return 0
    else:
        raise Exception("Wrong username or password")

def register(username, password):
    flag=0

    file = open("user_data.txt", "r+")

    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == username):
            flag = 1
            break

    if (flag): 
        raise Exception("Username already taken")

    if (not flag):
        file.write(username + ", " + password + "\n")
        return 0
    
    file.close()
    

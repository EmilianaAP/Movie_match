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

    if (success):
        print("Login Successful")
    else:
        print("wrong username or password")

    file.close()


def register(username, password):
    flag=0

    file = open("user_data.txt", "r+")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == username and b == password):
            flag = 1
            break

    if (flag == 0):
        print("Sign up sucessfully")
        file.write(username + "," + password + "\n")
    else: 
        print("Username already taken")

    file.close()

def access(option):
    if (option == "Login"):
        name = enter_username()
        password = enter_password()
        login(name, password)
    else:
        name = enter_username()
        password = enter_password()
        register(name, password)

def begin():
    global option
    option = input("Login or Register (Login,Sign_up): ")
    if (option != "Login" and option != "Sign_up"):
        begin()

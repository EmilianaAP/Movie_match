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
        print("Login Successful")
    else:
        print("wrong username or password")


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
        file.write("\n" + username + "," + password)
    else: 
        print("Username already taken")

    file.close()

def access(option):
    global name
    if (option == "Login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name, password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name, password)


def begin():
    global option
    option = input("Login or Register (Login,Sign_up): ")
    if (option != "Login" and option != "Sign_up"):
        begin()


begin()
access(option)

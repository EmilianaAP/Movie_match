from Registration import enter_username

def add_friend(username):
    friend = input("Enter your friends name")

    flag=0

    file = open("user_data.txt", "r+")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == friend):
            flag = 1
            break
    
    file.close()

    file = open("friend_data.txt", "a")

    if (flag == 1):
        print("Friend added sucessfully")
        file.write(username + ", " + friend + "\n")
    else: 
        print("This username does not exist")

    file.close()

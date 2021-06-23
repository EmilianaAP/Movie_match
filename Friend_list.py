from Registration import enter_username

def add_friend(username, friend):
    flag=0

    file = open("user_data.txt", "r+")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == friend):
            flag = 1
            break
    
    file.close()

    if (flag):
        file = open("friend_data.txt", "a")

        print("Friend added sucessfully")
        file.write(username + ", " + friend + "\n")

        file.close()
        return 0
    else: 
        raise Exception("This username does not exist")

    

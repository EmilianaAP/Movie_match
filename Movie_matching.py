def match(username, friend_username):
    friend_matches = []
    my_matches = []

    file = open("film_data.txt", "r")

    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if a == username:
            my_matches.append(b)
        elif a == friend_username:
            friend_matches.append(b)

    for i in my_matches:
        for x in friend_matches:
            if i == x:
                print("Matched movie: ", i)
    
    return 0
   
import Friend_list
import Movie_searching
import Movie_suggest
import Registration
import Movie_matching

print("To use MovieMatch you need to register in first.\n")
option = input("Do you have existing account(y/n): ")

if option == 'y':
    username = Registration.enter_username()
    password = Registration.enter_password()
    have_access = Registration.login(username, password)
    
    if(not have_access):
        print("Login Successful")

elif option == 'n':
    username = Registration.enter_username()
    password = Registration.enter_password()
    have_access = Registration.register(username, password)

    if(not have_access):
        print("Sign up sucessfully")

else:
    print("Error!")

while option != '4':
        option = input("\nMENU:\n\t(1)Search movie\n\t(2)Suggest movie\n\t(3)Match movie with friend\n\t(4)Exit\n")

        if option == '1':
            Movie_searching.movie_searching(username)
        elif option == '2':
            Movie_suggest.Suggest_movie(username)
        elif option == '3':
            to_add = input("Do you wanna add new friend (y/n): ")
            
            friend = input("Enter your friends name")

            if to_add == 'y':
                Friend_list.add_friend(username, friend)

            Movie_matching.match(username, friend)

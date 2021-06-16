from os import access

from requests.api import put
import Friend_list
import Movie_searching
import Movie_suggest
import Registration
import Movie_matching

print("To use MovieMatch you need to register in first.\n")
option = input("Do you have existing account(y/n): ")

if option == 'y':
    username = Registration.enter_username()
    have_access = Registration.login(username)
elif option == 'n':
    username = Registration.enter_username()
    have_access = Registration.register(username)
else:
    print("Error!")

if have_access == 0:
    while option != '4':
        option = input("\nMENU:\n\t(1)Search movie\n\t(2)Suggest movie\n\t(3)Match movie with friend\n\t(4)Exit\n")

        if option == '1':
            Movie_searching.movie_searching(username)
        elif option == '2':
            Movie_suggest.Suggest_movie(username)
        elif option == '3':
            to_add = input("Do you wanna add new friend (y/n): ")
            
            if to_add == 'y':
                Friend_list.add_friend(username)

            Movie_matching.match(username)
else:
    print("There is an error in your registration. Please try again later.")
    print("If you need help contact this email: 'ema.andr33va@gmail.com'\n")

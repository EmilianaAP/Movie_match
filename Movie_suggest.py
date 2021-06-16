import random
import requests
from bs4 import BeautifulSoup

def Suggest_movie(username):
    URL = 'http://www.imdb.com/chart/top'

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags]

    n_movies = len(titles)

    while(True):
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

        user_input = input("Do you want another movie (y/n)? ")
        if user_input != 'y':
            option = input("Do you want current movie to be added to your matched movies (y/n)? ")
            if option == 'y':
                file = open("film_data.txt", "a")

                print("Film added sucessfully")
                file.write(username + ", " + titles[idx] + "\n")
            break
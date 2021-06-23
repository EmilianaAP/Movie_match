from imdb import IMDb

def movie_searching(username):
    moviesDB = IMDb()

    movie_name = input("Enter movie name: ")
    movies = moviesDB.search_movie(movie_name)

    print('Searching for movies:')
    id = movies[0].getID()
    movie = moviesDB.get_movie(id)

    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    genre = movie['genres']

    print('Movie info:')
    print(f'{title} - {year}')
    print(f'rating: {rating}')
    print(f'genre: {genre}')

    option = input("Do you want this movie to be added to your matched movies (y/n)? ")
    if option == 'y':
        file = open("film_data.txt", "a")

        print("Film added sucessfully")
        file.write(username + ", " + title + "\n")
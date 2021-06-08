from imdb import IMDb

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

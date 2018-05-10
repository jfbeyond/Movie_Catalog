import media
import fresh_tomatoes

# This is the list of my 9 favorite movies
my_favorite = ['the lion king', 'little miss sunshine', 'jurassic park',
               'masaan', 'shrek 2', 'black panther',
               'dead poet society', 'hotel budapest', 'lord of the rings 3']

# Initialize the movie array that will contain my movies data
c = len(my_favorite)
movies = [None]*c

# Populate movies array with the data retrieved from API
for s in range(0, c):
    fav_id = media.Findmovie(my_favorite[s]).get_movie_id()
    movies[s] = media.Moviedata(fav_id).get_movie_data()

# Run the catalog website for my favorite movies
fresh_tomatoes.open_movies_page(movies)

# Print documentation for classes in media.py
print(media.Findmovie.__doc__)
print(media.Moviedata.__doc__)




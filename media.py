import tmdbsimple as tmdb
tmdb.API_KEY = '75efba297d4e1c34abc4d07ff269a878'


class Findmovie():
    """Find the movie id in the TMDB API to make the movie info
    request.

    Attributes:
        movie_name (str): Name of the movie to be found in the
        API.

    """
    def __init__(self, movie_name):
        self.movie_name = movie_name

    def get_movie_id(self):
        # Enable the tmdb API python wrapper search method
        # and retrieve the requested movie id
        search = tmdb.Search()  # Enables the Search method
        find_movie = search.movie(query=self.movie_name)
        movie_results = search.results
        movie_id = movie_results[0]['id']  # Get id from results
        return movie_id


class Moviedata():
    """Make the movie info request to the API based on the movie id
    by utilizing the Movies method of the tmdb API python wrapper.
    Return an array of four elements containing the movie title,
    storyline, poster url and youtube url.

    Attributes:
        movieid (int): id number of the movie found in the API

    """
    def __init__(self, movieid):
        self.movieid = movieid

    def get_movie_data(self):
        # This function retrieves the specific movie info fields to be
        # used in the catalog website.
        movie = tmdb.Movies(self.movieid)
        response = movie.info()
        poster = 'http://image.tmdb.org/t/p/w500/' + movie.poster_path
        storyline = movie.overview
        title = movie.title
        vid_response = movie.videos()
        vid_id = vid_response['results'][0]['key']
        trailer_youtube_url = 'https://www.youtube.com/watch?v=' + vid_id
        movie_package = [title, storyline, poster, trailer_youtube_url]
        return movie_package

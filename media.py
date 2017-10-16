import webbrowser
import tmdbsimple as tmdb


class Movie():
    """ This class generates and stores movie related information. """
    """ It takes TMDB movie id and a youtube URL (string) as arguments. """
    """ It returns the movie title, storyline, poster image,  """
    """ backdrop image, tagline, and rating, each through its own function. """

    # Assign API key for TMDB API
    tmdb.API_KEY = '1263dbac5a813170b2f4bc9c8e9fb168'

    # Initialize Movie class
    def __init__(self, movie_id, trailer_youtube):
        self.id = movie_id
        self.trailer_youtube_url = trailer_youtube

    # Functions to call movie title, storyline, poster image,
    # backdrop image, tagline, and rating (respectively)

    def get_title(self, movie_id):
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        return movie.title

    def get_storyline(self, movie_id):
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        return movie.overview

    def get_poster_img(self, movie_id):
        movie = tmdb.Movies(movie_id)
        resonse = movie.info()

        poster_img = 'https://image.tmdb.org/t/p/w500/' + movie.poster_path
        return poster_img

    def get_backdrop_img(self, movie_id):
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        backdrop_img = 'https://image.tmdb.org/t/p/w1000/' + movie.backdrop_path  # noqa
        return backdrop_img

    def get_tagline(self, movie_id):
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        return movie.tagline

    def get_rating(self, movie_id):
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        return movie.vote_average

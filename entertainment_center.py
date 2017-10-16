import fresh_tomatoes
import media
import tmdbsimple as tmdb

# Assign API key for TMDB API
tmdb.API_KEY = '1263dbac5a813170b2f4bc9c8e9fb168'

# Functions to call movie title, storyline, poster image,
# backdrop image, tagline, and rating (respectively)


def get_title(movie_id):
    movie = tmdb.Movies(movie_id)
    response = movie.info()

    return movie.title


def get_storyline(movie_id):
    movie = tmdb.Movies(movie_id)
    response = movie.info()

    return movie.overview


def get_poster_img(movie_id):
    movie = tmdb.Movies(movie_id)
    resonse = movie.info()

    poster_img = 'https://image.tmdb.org/t/p/w500/' + movie.poster_path
    return poster_img


def get_backdrop_img(movie_id):
    movie = tmdb.Movies(movie_id)
    response = movie.info()

    backdrop_img = 'https://image.tmdb.org/t/p/w1000/' + movie.backdrop_path
    return backdrop_img


def get_tagline(movie_id):
    movie = tmdb.Movies(movie_id)
    response = movie.info()

    return movie.tagline


def get_rating(movie_id):
    movie = tmdb.Movies(movie_id)
    response = movie.info()

    return movie.vote_average


# Instances of Movie class
nightmare_before = media.Movie(get_title(9479),
                               get_storyline(9479),
                               get_poster_img(9479),
                               get_backdrop_img(9479),
                               "https://www.youtube.com/watch?v=wr6N_hZyBCk",
                               get_tagline(9479),
                               get_rating(9479))

hocus_pocus = media.Movie(get_title(10439),
                          get_storyline(10439),
                          get_poster_img(10439),
                          get_backdrop_img(10439),
                          "https://www.youtube.com/watch?v=2UUMsInka2s",
                          get_tagline(10439),
                          get_rating(10439))


beetlejuice = media.Movie(get_title(4011),
                          get_storyline(4011),
                          get_poster_img(4011),
                          get_backdrop_img(4011),
                          "https://www.youtube.com/watch?v=euZTIOB9PhU",
                          get_tagline(4011),
                          get_rating(4011))

practical_magic = media.Movie(get_title(6435),
                              get_storyline(6435),
                              get_poster_img(6435),
                              get_backdrop_img(6435),
                              "https://www.youtube.com/watch?v=1pmSzGEqobo",
                              get_tagline(6435),
                              get_rating(6435))

corpse_bride = media.Movie(get_title(3933),
                           get_storyline(3933),
                           get_poster_img(3933),
                           get_backdrop_img(3933),
                           "https://www.youtube.com/watch?v=_tpLNUI9rQU",
                           get_tagline(3933),
                           get_rating(3933))

the_craft = media.Movie(get_title(9100),
                        get_storyline(9100),
                        get_poster_img(9100),
                        get_backdrop_img(9100),
                        "https://www.youtube.com/watch?v=oa-fbQ7SbyM",
                        get_tagline(9100),
                        get_rating(9100))

movies = [nightmare_before,
          hocus_pocus,
          beetlejuice,
          practical_magic,
          corpse_bride,
          the_craft]

fresh_tomatoes.open_movies_page(movies)

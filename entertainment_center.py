import fresh_tomatoes
import media


# Instances of Movie class
nightmare_before = media.Movie(9479,
                               "https://www.youtube.com/watch?v=wr6N_hZyBCk")

hocus_pocus = media.Movie(10439,
                          "https://www.youtube.com/watch?v=2UUMsInka2s")

beetlejuice = media.Movie(4011,
                          "https://www.youtube.com/watch?v=euZTIOB9PhU")

practical_magic = media.Movie(6435,
                              "https://www.youtube.com/watch?v=1pmSzGEqobo")

corpse_bride = media.Movie(3933,
                           "https://www.youtube.com/watch?v=_tpLNUI9rQU")

the_craft = media.Movie(9100,
                        "https://www.youtube.com/watch?v=oa-fbQ7SbyM")


# Note for Udacity reviewer:
# Decided not to load the instances into the movies array using a for loop
# because not all of the information is taken from the TMDB API (the
# youtube URL)

# Create an array to hold the instances of class Movie
movies = [nightmare_before,
          hocus_pocus,
          beetlejuice,
          practical_magic,
          corpse_bride,
          the_craft]

# Call function to open webpage using the Movie class instances
fresh_tomatoes.open_movies_page(movies)

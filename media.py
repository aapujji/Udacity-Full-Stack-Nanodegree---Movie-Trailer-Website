import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    
    def __init__(self, movie_title, movie_storyline, poster_image, backdrop_image, trailer_youtube, movie_tagline, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.backdrop_image_url = backdrop_image
        self.trailer_youtube_url = trailer_youtube
        self.tagline = movie_tagline
        self.rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

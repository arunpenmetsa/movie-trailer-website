import webbrowser
from datetime import date

# Each class has a __doc__ variable

# The movie class defines the title, storyline, image, trailer, rating
# and the release year for the movie

class Movie():
    """ This classs provides a way to store movie related information """
    
    # A list of all valid ratings
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    # Init function initializes all the variables
    def __init__(self, movie_title, movie_storyline,
                 poster_image,trailer_youtube, movie_rating, movie_release_year):   # self is the instance variable that is created    
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        # Check to make sure the movie rating is an accepted rating
        # else display a not available message
        try:
            b=Movie.VALID_RATINGS.index(movie_rating)
        except ValueError:
            self.rating = "NA"
        else:
            self.rating = movie_rating

        # Check to make sure the release year makes sense
        if int(movie_release_year) > date.today().year or int(movie_release_year) < 1896: 
            self.release_year = "NA"
        else:
            self.release_year = movie_release_year

    # Launch the trailer in the browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

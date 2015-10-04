import media
import fresh_tomatoes
from operator import attrgetter

# Create the Movie objects for titles to be displayed

shawshank_redemption = media.Movie(
        "Shawshank Redemption",
        "A story of an innocent man in prison",
        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
        "https://www.youtube.com/watch?v=6hB3S9bIaco",
        "R",
        "1994")

tora_tora_tora = media.Movie(
        "Tora Tora Tora",
        "The attack on Pearl Harbor during World War II",
        "https://upload.wikimedia.org/wikipedia/en/1/1a/ToraToraTora1970.png",  # noqa
        "https://www.youtube.com/watch?v=GgX1WBf2SjE",
        "G",
        "1970")

guardians_of_the_galaxy = media.Movie(
        "Guardians of the Galaxy",
        "Extraterrestrial Misfits fighting over a powerful artifact",
        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",  # noqa
        "https://www.youtube.com/watch?v=b3isCLVghoI",
        "PG-13",
        "2014")

return_of_the_king = media.Movie(
        "Return of the King",
        "Epic journey to destroy the one ring and evil on Middle Earth",
        "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",  # noqa
        "https://www.youtube.com/watch?v=WIrRJ8bCZYQ",
        "PG-13",
        "2003")

alien = media.Movie(
        "Alien",
        "Space Marines fight a deadly alien organism",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",  # noqa
        "https://www.youtube.com/watch?v=LjLamj-b0I8",
        "R",
        "1979")

gladiator = media.Movie(
        "Gladiator",
        "A Roman general is betrayed by the new Emperor",
        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # noqa
        "https://www.youtube.com/watch?v=uwTKRz-WmHU",
        "R",
        "2000")

# Create the list of movies
movies = [shawshank_redemption,
          tora_tora_tora,
          guardians_of_the_galaxy,
          return_of_the_king,
          alien,
          gladiator]

# Sort the list to show oldest movies first
movies_sort = sorted(movies, key=attrgetter('release_year'))

# Display the library
fresh_tomatoes.open_movies_page(movies_sort)

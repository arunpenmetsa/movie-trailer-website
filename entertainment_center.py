import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alient planet",
                        "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "storyline",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatoille = media.Movie("Ratatouille", "storyline",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie("Midnight in Paris", "storyline",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


hunger_games = media.Movie("Hunger Games", "storyline",
                        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


movies = [toy_story, avatar, school_of_rock, ratatoille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
# doc comes from a comment in the class definition

""" SE T38 compulsory task 2 """

import spacy

# Best spaCy model for similarity is loaded in.
nlp = spacy.load("en_core_web_md")

# Movies from movies.txt are read in and stored for later use.
with open("movies.txt", "r", encoding="utf-8") as movies:
    movie_list = movies.readlines()

# Last watched movie used for comparison.
PLANET_HULK = """
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""


def watch_next(recent_movie_desc: str) -> str:
    """Uses spaCy natural processing language model to find the similarity between
    a recently watched movie, to predict the next movie to watch.
    The title of the movie that best matches is returned."""

    recent_mov_token = nlp(recent_movie_desc)

    # Two empty lists are initiliased.
    film_selection = []

    mov_match_scores = []

    # Loops over the movie list taken from movies.txt.
    # Then extracts the film titles to one list
    # and the similarity scores to another.
    for movie in movie_list:

        film = movie.split(" :")

        film_selection.append(film[0])

        mov_token = nlp(movie)

        mov_match_scores.append(recent_mov_token.similarity(mov_token))

    # This gets the index of the highest number (best match) in the list of similarity scores.
    # Then uses the index to get the corresponding movie at that index in the film_selection list.
    best_movie_match = film_selection[mov_match_scores.index(max(mov_match_scores))]

    # The title of the best movie match is then returned as a string.
    return best_movie_match


print(
    f"Because you watched Planet Hulk, we suggest watching: {watch_next(PLANET_HULK)} next."
)

""" SE T38 compulsory task 1 """

import spacy

nlp = spacy.load("en_core_web_md")  # advanced language model for semantic similarity

# nlp = spacy.load('en_core_web_sm') # simpler language model for NLP

# word1 = nlp("cat")

# word2 = nlp("monkey")

# word3 = nlp("banana")

word1 = nlp("dolphin")

word2 = nlp("cobra")

word3 = nlp("rock")

print(word1.similarity(word2))

print(word3.similarity(word2))

print(word3.similarity(word1))

# NOTE - Similarity between cat, monkey and banana.
# The results are floats.
# This is interesting because it looks like the results could be displayed as a percentage.
# A perfect match (The exact same word), equals 1, so therefore is a 100% match.
# What surprises me is that cat and monkey have a 0.59 match,
# I suppose that must be because they are both mammals.

# NOTE - my example - Similarity between dolphin, cobra and rock.
# I am surprised that the last two showed any similarity:
# rock and dolphin - score 0.22. Perhaps the similarity was that they are not human, or share one chemical component.
# rock and cobra - score 0.19. same as above, although, it seems to have a lower similarity.
# I am not surprised that dolphin and cobra showed the highest similarity though,
# as they are animals, even if they are different species.


# NOTE - 'en_core_web_sm' difference to 'en_core_web_md'

# This error was raised, when it ran:
# UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger,
# parser and NER, which may not give useful similarity judgements.
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`,
# which don't ship with word vectors and only use context-sensitive tensors.
# You can always add your own word vectors, or use one of the larger models instead if available.

# My Thoughts:
# The results were higher with en_core_web_md.
# Especially in the third section, when the recipes and complaints were compared.
# If you look at the text with human eyes, there are large differences in both texts.
# This could lead you to believe that en_core_web_sm is more accurate, as it shows a lower score for similarity.
# However it is clear that is not about the similarity on the surface area but the ability to find deeper similarities.
# Therefore 'en_core_web_md' is a much better langauge model.

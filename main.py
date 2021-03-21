#!/usr/bin/python3 

from similarity.normal import NormalStringSimilarity
from similarity.word2vec import Word2VecSimilarity

# similaritier = Word2VecSimilarity(modelPath='./data/models/similarity/GoogleNews-vectors-negative300.bin')
# print(similaritier.matching("you have a cunt face", "you are a tml"))
similaritier = NormalStringSimilarity()
print(similaritier.matching("you have a cunt face", "you are a tml"))
import numpy as np
from gensim.models import KeyedVectors
from gensim.models.word2vec import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from pyvi import ViTokenizer

class Word2VecSimilarity :

    def __init__(self, lang='en', isTokenize=False, modelPath=None):
        self.__lang = lang
        self.__modelPath = modelPath
        self.__isTokenize = isTokenize
        if modelPath is not None : self.__loadModel()

    def __tokenize(self, sentence) :
        if self.__isTokenize :
            if self.__lang == 'vi': 
                sentence = ViTokenizer.tokenize(sentence)
        return sentence.split()

    def __loadModel(self) :
        print("Loading model '{0}'...".format(self.__modelPath))
        self.__model = KeyedVectors.load_word2vec_format(self.__modelPath, binary=True)
        print("Loaded!")

    def __sentence2vector(self, sentence) :
        words = self.__tokenize(sentence)
        vector_result = sum([self.__model.get_vector(word) for word in words if word in self.__model.wv])
        vector_result = vector_result / len(words)
        return vector_result.reshape(1, -1)

    def __get_vector(self, sentence):
        vector = self.__sentence2vector(sentence)
        return vector
    
    def matching(self, sentence1, sentence2) :
        return cosine_similarity(self.__get_vector(sentence1), self.__get_vector(sentence2))[0][0]

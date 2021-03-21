#!/usr/bin/python3
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

class NormalStringSimilarity :

    def __init__(self, remove_stopwords=False):
        self.__remove_stopwords = remove_stopwords
        self.__stemmer = nltk.stem.porter.PorterStemmer()
        self.__remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
        self.__vectorizer = TfidfVectorizer(tokenizer=self.__normalize)
        nltk.download('punkt') # if necessary...


    def matching(self, text1, text2) :
        tfidf = self.__vectorizer.fit_transform([text1, text2])
        return ((tfidf * tfidf.T).A)[0,1]

    def __stemTokens(self, tokens):
        return [self.__stemmer.stem(item) for item in tokens]

    def __normalize(self, text):
        return self.__stemTokens(nltk.word_tokenize(text.lower().translate(
            self.__remove_punctuation_map
        )))


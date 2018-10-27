#!/usr/bin/python
""" preprocessing

Text preprocessing: Data wrangling and text vectorization.

Author: datadonk23
Date: 24.10.18 
"""

import re
import unicodedata

from sklearn.datasets import load_files
from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
nltk.download(["punkt", "wordnet"], download_dir="nltk/")
nltk.data.path.append("nltk/")
from nltk import wordpunct_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


class TextWrangler(object):
    """ Clean and tokenize documents.

    Tokenize documents. Removes punctuation and stopwords.
    Converts tokens to lowercase. Replaces numbers with generic number token.
    Depending on `kind` parameter, stems or lemmatizes tokens.

    Parameters
    ----------
    kind : str
        Either "stem" (default) for stemming or "lemma" for lemmatization

    """

    def __init__(self, kind="stem"):
        self.kind = kind
        self.stemmer = LancasterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        sklearn_stopwords = stop_words.ENGLISH_STOP_WORDS
        custom_stopwords = ["arthur", "conan", "doyle", "chapter", "contents",
                            '`--"', "`"]
        self.stopwords = sklearn_stopwords.union(custom_stopwords)

    def __call__(self, document):
        if self.kind == "lemma":
            tokens = [self.lemmatizer.lemmatize(token.lower())
                      for token in wordpunct_tokenize(document)
                      if not self.is_punct(token)
                      and not self.is_singlechar(token)
                      and not self.is_stopword(token.lower())]
        else:
            tokens = [self.stemmer.stem(token.lower())
                      for token in wordpunct_tokenize(document)
                      if not self.is_punct(token)
                      and not self.is_singlechar(token)
                      and not self.is_stopword(token.lower())]

        clean_tokens = ["NUM" if self.is_number(token) else token
                        for token in tokens]

        return clean_tokens

    def is_punct(self, token):
        return all(unicodedata.category(char).startswith("P") for char in token)

    def is_singlechar(self, token):
        return len(token) < 2

    def is_stopword(self, token):
        return token in self.stopwords

    def is_number(self, token):
        return bool(re.match(r"\d+", token))


def load_corpus(path):
    """ Loads corpus from specified directory.

    :param path: String - directory
    :return: raw_corpus : Bunch - object of documents
    """
    raw_corpus = load_files(path)

    return raw_corpus


def tfidf_vectorizer():
    """ Initializes tfidf vectorizer

    :return: TfidfVectorizer object
    """
    tfidf = TfidfVectorizer(strip_accents="ascii",
                            tokenizer=TextWrangler(kind="stem"))

    return tfidf

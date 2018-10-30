#!/usr/bin/python
""" test_preprocessing

Author: datadonk23
Date: 24.10.18 
"""

import unittest

from sklearn.feature_extraction.text import TfidfVectorizer

from preprocessing import TextWrangler, load_corpus, tfidf_vectorizer


class TestTextWrangler(unittest.TestCase):
    def setUp(self):
        self.wrangler = TextWrangler()
        self.lemma_wrangler = TextWrangler(kind="lemma")

    def test_is_punct(self):
        self.assertTrue(self.wrangler.is_punct(token="."),
                        "Dot should be punct")
        self.assertTrue(self.wrangler.is_punct(token=".!?,"),
                        "Multiple punct token should be punct")

    def test_is_singlechar(self):
        self.assertTrue(self.wrangler.is_singlechar(token="t"),
                        "Single char 't' should be singlechar")
        self.assertFalse(self.wrangler.is_singlechar(token="tt"),
                        "Chars 'tt' should not be singlechar")

    def test_is_stopword(self):
        self.assertTrue(self.wrangler.is_stopword(token="is"),
                        "'is' should be stopword")
        self.assertTrue(self.wrangler.is_stopword(token="chapter"),
                        "'chapter' should be stopword")
        self.assertFalse(self.wrangler.is_stopword(token="norbury"),
                        "'norbury' should not be stopword")

    def test_is_number(self):
        self.assertTrue(self.wrangler.is_number(token="23"),
                        "23 should be a number")
        self.assertTrue(self.wrangler.is_number(token="110th"),
                        "110th should be a number")
        self.assertFalse(self.wrangler.is_number(token="datadonK23"),
                        "datadonK23 should not be a number")

    def test_call(self):
        testcase_stem = self.wrangler.__call__(
            "There is nothing more deceptive than an obvious fact.")
        expected_stem = ["deceiv", "obvy", "fact"]
        testcase_lemma = self.lemma_wrangler.__call__(
            "There is nothing more deceptive than an obvious fact.")
        expected_lemma = ["deceptive", "obvious", "fact"]

        self.assertEqual(testcase_stem, expected_stem,
                         "False tokenization by stem wrangler")
        self.assertEqual(testcase_lemma, expected_lemma,
                         "False tokenization by stem wrangler")


class TestInput(unittest.TestCase):
    def test_load_corpus(self):
        corpus = load_corpus("data/")

        self.assertEqual(len(corpus.data), 56,
                         "Wrong number of documents loaded")


class TestVectorizer(unittest.TestCase):
    def test_tfidf_vectorizer(self):
        vectorizer = tfidf_vectorizer()

        self.assertEqual(type(vectorizer), TfidfVectorizer,
                         "Vectorizer does not return tfidf vectorizer object")
        self.assertFalse(hasattr(vectorizer, "vocabulary_"),
                         "Tfidf object should be untrained, but has vocab")


if __name__ == '__main__':
    unittest.main()

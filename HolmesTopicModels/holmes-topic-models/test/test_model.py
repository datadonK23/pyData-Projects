import unittest
from unittest.mock import patch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

from preprocessing import tfidf_vectorizer
from model import make_pipeline, make_model


class TestMakeModel(unittest.TestCase):
    def test_make_model(self):
        model = make_model()
        model_3_topics = make_model(3)

        self.assertEqual(model.n_components, 5,
                         "False default num of components")
        self.assertEqual(model_3_topics.n_components, 3,
                         "False num of components passed to model")
        self.assertEqual(model.solver, "mu",
                         "False solver in model")
        self.assertEqual(model.beta_loss, "kullback-leibler",
                         "False kind of beta loss")
        self.assertEqual(model.alpha, 0.1,
                         "False alpha value")


class TestMakePipeline(unittest.TestCase):
    def setUp(self):
        self.vectorizer = tfidf_vectorizer()
        self.model = make_model()

    def test_make_pipeline(self):
        pipe = make_pipeline(self.vectorizer, self.model)

        self.assertEqual(pipe.steps[0][0], "tfidf",
                         "False vectorizer step name")
        self.assertEqual(pipe.steps[1][0], "nmf",
                         "False model step name")
        self.assertIsInstance(pipe.steps[0][1], TfidfVectorizer,
                              "Vectorizer not an instance of TfidfVectorizer")
        self.assertIsInstance(pipe.steps[1][1], NMF,
                              "Model not an instance of NMF")


def main():
    unittest.main()

if __name__ == "__main__":
    main()
 

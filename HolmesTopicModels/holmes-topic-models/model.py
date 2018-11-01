#!/usr/bin/python
""" model

Model and pipeline building

Author: datadonk23
Date: 23.10.18 
"""

from sklearn.pipeline import Pipeline
from sklearn.decomposition import NMF


def make_model(n_topics=5):
    """ Creates sklearn NMF model

    :param n_topics: number of topics
    :return: model object
    """
    model = NMF(n_components=n_topics,
                solver="mu", beta_loss="kullback-leibler", alpha=0.1,
                random_state=23)

    return model


def make_pipeline(tfidf_vectorizer, model):
    """ Creates sklearn NLP pipeline

    :param vectorizer: Vectorizer object
    :param model: Model object
    :return: Pipeline object
    """
    tfidf_vectorizer = tfidf_vectorizer
    model = model

    pipeline = Pipeline([("tfidf", tfidf_vectorizer),
                         ("nmf", model)])

    return pipeline

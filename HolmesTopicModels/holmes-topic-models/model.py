#!/usr/bin/python
""" model

#FIXME Description

Author: datadonk23
Date: 23.10.18 
"""
import os

from sklearn.externals import joblib


class Model:
    """
        Trained model: #FIXME
        Methods:
            predict(input) - predicts target class based on given input
    """

    def __init__(self):
        actual_filepath = os.path.dirname(os.path.realpath(__file__))
        # model_file = os.path.join(actual_filepath, "data/model_trained.pkl")
        # self.trained_model = joblib.load(model_file)

    def predict(self, input):
        """
        Predicts target class based on given input
        :param input: #FIXME
        :return: #FIXME
        """
        pred = self.trained_model.predict(input)

        return pred


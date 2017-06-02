""" 
    MODEL: trained Decision Tree CV
"""
import os

from sklearn.externals import joblib

class Model:
    """
        Trained model: Decision Tree CV
        Methods:
            predict(input) - predicts target class based on given input
    """
    def __init__(self):
        actual_filepath = os.path.dirname(os.path.realpath(__file__))
        model_file = os.path.join(actual_filepath, "data/model_trained.pkl")
        self.trained_model = joblib.load(model_file)

    def predict(self, input):
        """
        Predicts target class based on given input
        :param input: np.array([[Int, Int, Int]])
        :return: Int (0|1; 0 => "should not attend", 1 => "should attend")
        """
        pred = self.trained_model.predict(input)

        return pred


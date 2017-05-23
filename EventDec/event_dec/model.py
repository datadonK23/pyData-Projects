""" 
    MODEL: trained Decision Tree CV
"""
from sklearn.externals import joblib

class Model:
    """
        Trained model: Decision Tree CV
        Methods:
            predict(input) - predicts target class based on given input
    """
    def __init__(self):
        self.trained_model = joblib.load("data/model_trained.pkl")

    def predict(self, input):
        """
        Predicts target class based on given input
        :param input: np.array([[Int, Int, Int]])
        :return: Int (0|1; 0 => "should not attend", 1 => "should attend")
        """
        pred = self.trained_model.predict(input)

        return pred


import unittest
from unittest.mock import patch
import numpy as np

from project.model import Model #FIXME

class ModelTests(unittest.TestCase):
    @patch.object(project.main.make_input, "input", create=True) #FIXME
    def test_predict(self, input):
        """
        Test #FIXME
        """
        input.return_value = input_for_test = np.array([[#FIXME]])
        model = Model()

def main():
    unittest.main()

if __name__ == "__main__":
    main()
 

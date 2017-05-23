import unittest
from unittest.mock import patch
import numpy as np

import event_dec
from event_dec.model import Model

class ModelTests(unittest.TestCase):

    @patch.object(event_dec.main.clean_input, "input", create=True)
    def test_predict(self, input):
        input.return_value = input_attend = np.array([[0, 1, 4]])
        input.return_value = input_notattend = np.array([[1, 0, 0]])
        model = Model()

        self.assertIsNotNone(model.predict(input=input_notattend), "Returns not None")

        self.assertIn(model.predict(input=input_attend), [0,1], "Returns either 0 or 1")

        expected_attend = 1
        actual_attend = model.predict(input=input_attend)
        self.assertEqual(expected_attend, actual_attend, "Attend event")

        expected_notattend = 0
        actual_notattend = model.predict(input=input_notattend)
        self.assertEqual(expected_notattend, actual_notattend, "Not attend event")


def main():
    unittest.main()

if __name__ == "__main__":
    main()

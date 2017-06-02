import unittest
from unittest.mock import patch

import sys
import numpy as np

from event_dec.main import get_input, process_input, print_output


class MainTests(unittest.TestCase):
    def test_get_input(self):
        """
        Test input handling and correct returns
        """
        # Returns None quit App, if too many (5) false inputs are provided
        with patch("builtins.input", side_effect=["", "", "", "", ""]):
            expected = None
            actual = get_input()
            self.assertEqual(expected, actual, "Too many false inputs, returns None")
        with patch("builtins.input", side_effect=["", " ", "False", " ", 0, "", "", " ", 1, "False"]):
            expected = None
            actual = get_input()
            self.assertEqual(expected, actual, "Too many false inputs, returns None")

        # Stop iterating when false input 1
        with patch("builtins.input", side_effect=[None, 0, 23]):
            with self.assertRaises(StopIteration, msg="No 1st input, but doesn't stop iterating"):
                get_input()
        with patch("builtins.input", side_effect=["", 0, 23]):
            with self.assertRaises(StopIteration, msg="1st input incorrect (empty string), but doesn't stop iterating"):
                get_input()

        # Stop iterating when false input 2
        with patch("builtins.input", side_effect=["String", "False", 23]):
            with self.assertRaises(StopIteration, msg="2nd input incorrect, but doesn't stop iterating"):
                get_input()
        with patch("builtins.input", side_effect=["String", 3, 23]):
            with self.assertRaises(StopIteration, msg="2nd input incorrect (out of range), but doesn't stop iterating"):
                get_input()
        with patch("builtins.input", side_effect=["String", -1, 23]):
            with self.assertRaises(StopIteration, msg="2nd input incorrect (negative input), but doesn't stop iterating"):
                get_input()

        # Stop iterating when false input 3
        with patch("builtins.input", side_effect=["String", 0, "False"]):
            with self.assertRaises(StopIteration, msg="3rd input incorrect (String), but doesn't stop iterating"):
                get_input()
        with patch("builtins.input", side_effect=["String", 0, -23]):
            with self.assertRaises(StopIteration, msg="3rd input incorrect (negative input), but doesn't stop iterating"):
                get_input()

        # TypeError input 2
        with patch("builtins.input", side_effect=["String", None, 23]):
            with self.assertRaises(TypeError, msg="No 2nd input, but no TypeError raised"):
                get_input()

        # TypeError input 3
        with patch("builtins.input", side_effect=["String", 0, None]):
            with self.assertRaises(TypeError, msg="No 3rd input, but no TypeError raised"):
                get_input()

        # Returns correct raw_input tuple
        with patch("builtins.input", side_effect=["String", 1, 23]):
            expected = ("String", 1, 23)
            actual = get_input()
            self.assertTupleEqual(expected, actual, "Returns correct tuple")
        with patch("builtins.input", side_effect=["String 2", 0, 0]):
            expected = ("String 2", 0, 0)
            actual = get_input()
            self.assertTupleEqual(expected, actual, "Returns correct tuple")


    @patch.object(get_input, "raw_input", create=True)
    def test_process_input(self, raw_input):
        """
        Test for correct processing and return types
        """
        raw_input.return_value = input_emptyTitle = (" ", 0, 1) # None case excluded in get_input()
        raw_input.return_value = input_buzzword = ("Design Thinking", 0, 1)
        raw_input.return_value = input_noBuzzword = ("String", 1, 400)
        raw_input.return_value = input_distanceBin0Home = ("String", 0, 0)
        raw_input.return_value = input_distanceBin0 = ("String", 0, 9)
        raw_input.return_value = input_distanceBin1 = ("String", 0, 10)
        raw_input.return_value = input_distanceBin2 = ("String", 0, 40)
        raw_input.return_value = input_distanceBin3 = ("String", 0, 120)
        raw_input.return_value = input_distanceBin4 = ("String", 0, 180)
        raw_input.return_value = input_distanceBin4ZHR = ("String", 0, 454)

        # Test empty title input
        expected_emptyTitle = np.array([[0, 0, 0]])
        actual_emptyTitle = process_input(input_emptyTitle)
        np.testing.assert_array_equal(expected_emptyTitle, actual_emptyTitle, err_msg="No buzzword in empty title")

        # Test buzzword processing
        expected_buzzwordy = np.array([[1, 0, 0]])
        actual_buzzwordy = process_input(input_buzzword)
        # testing array equality
        np.testing.assert_array_equal(expected_buzzwordy, actual_buzzwordy, err_msg="Buzzword in input title")

        expected_notBuzzwordy = np.array([[0, 1, 4]])
        actual_notBuzzwordy = process_input(input_noBuzzword)
        np.testing.assert_array_equal(expected_notBuzzwordy, actual_notBuzzwordy, err_msg="No buzzword in input title")

        # Test distance binning
        expected_distanceBin0Home = np.array([[0, 0, 0]])
        actual_distanceBin0Home = process_input(input_distanceBin0Home)
        np.testing.assert_array_equal(expected_distanceBin0Home, actual_distanceBin0Home,
                                      err_msg="Distance 0 should be bin 0")

        expected_distanceBin0 = np.array([[0, 0, 0]])
        actual_distanceBin0 = process_input(input_distanceBin0)
        np.testing.assert_array_equal(expected_distanceBin0, actual_distanceBin0,
                                      err_msg="Distance 10 should be bin 0")

        expected_distanceBin1 = np.array([[0, 0, 1]])
        actual_distanceBin1 = process_input(input_distanceBin1)
        np.testing.assert_array_equal(expected_distanceBin1, actual_distanceBin1,
                                      err_msg="Distance 11 should be bin 1")

        expected_distanceBin2 = np.array([[0, 0, 2]])
        actual_distanceBin2 = process_input(input_distanceBin2)
        np.testing.assert_array_equal(expected_distanceBin2, actual_distanceBin2,
                                      err_msg="Distance 41 should be bin 2")

        expected_distanceBin3 = np.array([[0, 0, 3]])
        actual_distanceBin3 = process_input(input_distanceBin3)
        np.testing.assert_array_equal(expected_distanceBin3, actual_distanceBin3,
                                      err_msg="Distance 121 should be bin 3")

        expected_distanceBin4 = np.array([[0, 0, 4]])
        actual_distanceBin4 = process_input(input_distanceBin4)
        np.testing.assert_array_equal(expected_distanceBin4, actual_distanceBin4,
                                      err_msg="Distance 181 should be bin 4")

        expected_distanceBin4ZHR = np.array([[0, 0, 4]])
        actual_distanceBin4ZHR = process_input(input_distanceBin4ZHR)
        np.testing.assert_array_equal(expected_distanceBin4ZHR, actual_distanceBin4ZHR,
                                      err_msg="Distance to ZHR should be bin 4")


    def test_print_output(self):
        """
        Test for correct output
        """
        mocked_predAttend = np.array([1])
        print_output(mocked_predAttend)
        actual_outputAttend = sys.stdout.getvalue().strip().splitlines()[-1]
        expected_outputAttend = "Predicted Class: [1]. You should attend the event, it'll probably be worth the time."
        self.assertEqual(expected_outputAttend, actual_outputAttend, "Case attend: incorrect Output")

        mocked_predNotAttend = np.array([0])
        print_output(mocked_predNotAttend)
        actual_outputNotAttend = sys.stdout.getvalue().strip().splitlines()[-1]
        expected_outputNotAttend = "Predicted Class: [0]. You shouldn't attend this event, it'll probably be a waste of time."
        self.assertEqual(expected_outputNotAttend, actual_outputNotAttend, "Case not attend: incorrect Output")


def main():
    unittest.main()

if __name__ == "__main__":
    main()

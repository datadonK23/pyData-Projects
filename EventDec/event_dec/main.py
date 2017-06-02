#!/usr/bin/python

import numpy as np
import pickle
import os

from model import Model

def get_input():
    """
    Ask user for inputs about event: Title, Main Topic, Distance to Location.
    Checks for correct types and value ranges. If not correct, restarts asking 5 times.
    :return: Tuple(Str, Int, Int) => "Title", [0|1], [0,infinity[ OR None (to quit App)
    """
    attempt = 0
    title, topic, distance = None, None, None

    while True:
        """ Here be dragons """
        if attempt >= 5: # Stop asking, if too many false inputs
            print("Too many false inputs. Stopping application.")
            return None
            break
        else: # Title of Event?
            title = input("Title of event: ")
            if not title:
                print("No valid title entered. Try again!")
                attempt += 1
                continue
            else:
                try: # Main Topic Data?
                    topic = int(input("Is the main topic of event 'Data'? (0=no | 1=yes): "))
                    if topic not in {0, 1}:
                        print("Input must be 0 or 1. Try again!")
                        attempt += 1
                        continue
                except ValueError:
                    print("Input must be an Integer (0 or 1). Try again!")
                    attempt += 1
                    continue
                try: # Distance to Location?
                    distance = int(float(input("How far away is the location? (km): ")))
                    if distance < 0:
                        print("Input must be a positive number. Try again!")
                        attempt += 1
                        continue
                except ValueError:
                    print("Input must be an Integer (distance in km). Try again!")
                    attempt += 1
                    continue
        break

    return title, topic, distance


def process_input(raw_input):
    """
    Process title field - check if title contains buzzword.
    Process distance field - bins distance value in bins=[10, 40, 120, 180], which correspond to distances from 
        homelocation to Steyr, Linz, Salzburg, Vienna, >Vienna
    Convert to correct input format for model.
    :param raw_input: Tuple(Str, Int, Int) => "Title", [0|1], [0,infinity[
    :return: np.array([[Int, Int, Int]]) => [0|1], [0|1], [0,4]
    """

    input = np.zeros(shape=(1, 3), dtype=np.int)
    input[0, 0] = 0 # default not buzzwordy
    input[0, 1] = int(raw_input[1])
    distance_raw = int(raw_input[2])

    # Process title
    title_str = raw_input[0]
    actual_filepath = os.path.dirname(os.path.realpath(__file__))
    buzzword_file = os.path.join(actual_filepath, "data/buzzword_list.pkl")

    with open(buzzword_file, "rb") as f:
        buzzword_list = pickle.load(f)

    for buzzword in buzzword_list:
        if buzzword.lower() in title_str.lower():
            input[0, 0] = 1 # buzzwordy
            break

    # Process distance
    distance_bins = [10, 40, 120, 180]  # SR, LNZ, SZG, VIE, >VIE
    input[0, 2] = np.digitize(distance_raw, bins=distance_bins)

    return input


def print_output(pred):
    """
    Takes predicted Value (0="should not attend" | 1="should attend") from Model and prints a recommendation to stdout.
    :param pred: np.ndarray([Int]) => [0] "should not attend" | [1] "should attend"
    :return: -
    """
    if pred == np.array([0]):
        print("Predicted Class: {}. You shouldn't attend this event, it'll probably be a waste of time.".format(str(pred)))
    elif pred == np.array([1]):
        print("Predicted Class: {}. You should attend the event, it'll probably be worth the time.".format(str(pred)))
    else: # shouldn't happen
        print("Sorry, something went wrong with your prediction. Try again.")


def main():
    """
    Main Loop
    :return: -
    """
    raw_input = get_input()
    if raw_input:
        input = process_input(raw_input)
        try:
            """ Here be dragons """
            model = Model()
            pred = model.predict(input=input)
            print_output(pred=pred)
        except:
            print("Couldn't predict value. Quit Application.")
    else:
        print("Quit Application")


if __name__ == "__main__":
    main()
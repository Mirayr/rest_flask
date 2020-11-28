# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd


def load_data():
    data = pd.read_csv('../dumps/squark_amazon_alexa_multiclass_production_data.csv', encoding='ISO 8859-1')
    data_training = pd.read_csv('../dumps/squark_amazon_alexa_multiclass_training_data.csv', encoding='ISO 8859-1')
    return data, data_training


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Mirayr')
    print(np.ones((5, 5)))
    a, b = load_data()
    print(a.head())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

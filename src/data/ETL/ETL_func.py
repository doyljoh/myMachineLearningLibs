# -*- coding: utf-8 -*-
"""
Functions that are used within ETL

Author: John Doyle
"""

import json
import pandas as pd



def load_config_json(dataFilePath):
    """
    This function loads a json configuration file, which is used to store user
    defined parameters/variables

    :param dataFilePath: The full path and file name of the configuration file
    :return: A dictornary containing configuration parameters for ETL
    """

    with open(dataFilePath) as jsonFile:
        jsonData = json.load(jsonFile)
        return jsonData["ETL"]


def load_data_csv(dataFilePath, readConfig):
    """
    This function loads data from a csv file into a pandas dataframe

    :param dataFilePath: The full path and file name of the csv to be loaded
    :param readConfig: The configuration parameter to pass to read_csv
    :return: A pandas dataframe
    """

    df = pd.read_csv(dataFilePath, readConfig)
    return readConfig
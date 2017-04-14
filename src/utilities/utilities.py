# -*- coding: utf-8 -*-
"""
Utility Functions that are used across all process stages

Author: John Doyle
"""

import json
import pandas as pd
import logging
from time import gmtime, strftime
from sklearn.model_selection import train_test_split

log = logging.getLogger(__name__)


def load_config_json(dataFilePath,key):
    """
        This function loads a json configuration file, which is used to store user
        defined parameters/variables
    
        :param dataFilePath: The full path and file name of the configuration file
        :return: A dictornary containing configuration parameters for the key
    """

    log.info("{0}: load_data_csv: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dataFilePath))
    log.info("{0}: load_data_csv: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), key))

    with open(dataFilePath) as jsonFile:
        jsonData = json.load(jsonFile)
        return jsonData[key]


def load_data_csv(dataFilePath, readConfig):
    """
        This function loads data from a csv file into a pandas dataframe
    
        :param dataFilePath: The full path and file name of the csv to be loaded
        :param readConfig: The configuration parameter to pass to read_csv
        :return: A pandas dataframe
    """

    log.info("{0}: load_data_csv: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dataFilePath))
    log.info("{0}: load_data_csv: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), readConfig.items()))

    df = pd.read_csv(dataFilePath, *readConfig)
    log.info("{0}: df: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), list(df)))

    return df


def split_dataframe(dfInput, splitCongif):
    """
        This function splits a data pandas dataframe into chunks
    
        :param dfInput: The pandas dataframe to be split
        :param splitCongif: The splitting configuration parameters
        :return: A list containing split data frames
    """

    log.info("{0}: split_dataframe: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dfInput.head()))
    log.info("{0}: split_dataframe: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), splitCongif))

    if splitCongif["type"] == "random":
        df_train, df_test = train_test_split(dfInput, train_size=splitCongif["train_size"])
        log.info("{0}: Row Count [dfInput,df_train,df_test]: [{1},{2},{3}]".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dfInput.shape[0],df_train.shape[0],df_test.shape[0]))


    return [df_train, df_test]
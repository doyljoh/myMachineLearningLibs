# -*- coding: utf-8 -*-
"""
Functions that are used within ETL

Author: John Doyle
"""

import logging
from time import gmtime, strftime
import os
from os import listdir
from os.path import isfile, join
from ...utilities import utilities as util

log = logging.getLogger(__name__)


def split_numer_datasets(dataPath, etlConfig):
    """
        This function scans a directory for files, and and returns a a json configuration file, which is used to store user
        defined parameters/variables

        :param dataPath: The full directory path of numer training data
        :param dataPath: The ETL configuration parameters  
    """

    log.info("{0}: split_numer_datasets: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dataPath))
    log.info("{0}: etlConfig: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), etlConfig))

    # Get all files in folder, save to list and merge with path
    files = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]

    # Set paths of where to save spit dataframes
    rawDir = os.path.abspath(os.path.join(dataPath, os.pardir))
    outTrainDir = os.path.join(rawDir, "split_training")
    outTestDir = os.path.join(rawDir, "split_test")

    for f in files:

        # Load each training file
        df_numerData = util.load_data_csv(os.path.join(dataPath, f), etlConfig["Load"])

        # Split each dataframe and save to file
        df_train, df_test = util.split_dataframe(df_numerData, etlConfig["Split"])

        #output files to training and test folders
        df_train.to_csv(outTrainDir+"/"+f, sep=',', index=False)
        df_test.to_csv(outTestDir+"/"+f, sep=',', index=False)






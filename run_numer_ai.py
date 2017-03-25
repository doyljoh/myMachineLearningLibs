# -*- coding: utf-8 -*-
"""
Build a classifier to perform binary classification of Numerai data

Author: John Doyle
"""

import sys
import os
import logging
from time import gmtime, strftime

#add local cod directories
sys.path.append("../src")
from data import make_dataset

def main():

    #set paths
    cwd = os.getcwd()
    dirLogs = os.path.join(cwd, "logs")
    dirData = os.path.join(cwd, "data")
    dirModels = os.path.join(cwd, "models")
    dirReports = os.path.join(cwd, "reports")

    #set logging parameters
    logging.basicConfig(filename = dirLogs+'/run_numer_ai.log', level=logging.DEBUG)
    logging.info("{0}: Starting run_numer_ai".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    logging.info("{0}: Data Directory {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),dirData))
    logging.info("{0}: Model Directory {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dirModels))
    logging.info("{0}: Report Directory {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dirReports))

    # Run ETL
    make_dataset("/home/john/Projects/RepoNumerAI/data/Configs/config_NumerAI_v1.json")


    # Load Datasets
    logging.info("{0}: Load datasets into memory".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    # Create Training, Test and Validation Datasets
    logging.info("{0}: Create Training, Test and Validation Datasets".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    # Clean data and build features dataset
    logging.info("{0}: Clean data and build features datasets".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    # Train Models and Optimise
    logging.info("{0}: Train Models and Optimise".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    # Predict Competition Scores and output Results
    logging.info("{0}: Predict Competition Scores and output Results".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))



if __name__ == '__main__':
    main()
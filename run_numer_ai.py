# -*- coding: utf-8 -*-
"""
Build a classifier to perform binary classification of Numerai data

Author: John Doyle
"""

import os
import logging
from time import gmtime, strftime

#add local cod directories
from src.dataPrep.run_ETL import ETL
from src.features.build_features import FE

def main():

    #set paths
    cwd = os.path.abspath(os.path.join(os.curdir))

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

    #Run ETL
    etl = ETL(dirData + "/Configs/config_NumerAI_v1.json")
    if etl.config["run"]=="True":
        etl.numer(dirData + "/raw/")

    #Build Features
    fe = FE(dirData + "/Configs/config_NumerAI_v1.json")
    if fe.config["run"]=="True":
        fe.numer(dirData + "/raw/")

    # Train Models and Optimise
    #logging.info("{0}: Train Models and Optimise".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    # Predict Competition Scores and output Results
    #logging.info("{0}: Predict Competition Scores and output Results".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))


if __name__ == '__main__':
    main()
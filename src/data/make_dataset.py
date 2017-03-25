# -*- coding: utf-8 -*-
"""
Perform ETL operations of Numerai datasets, to perpare the data for modeling

Author: John Doyle
"""


import logging
from ETL import ETL_func
from time import gmtime, strftime


class ETL:


    def __init__(self, configFilePath):

        #load configuration file
        self.config = ETL_func.load_config_json(configFilePath)
        logging.info("{0}: ETL Configuration: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),self.config))



def main(configFilePath):
    """ Runs ETL processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    # set paths
    logging.info("{0}: Running ETL".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    # create ETL Object
    objETL = ETL(configFilePath)





if __name__ == '__main__':

    main()

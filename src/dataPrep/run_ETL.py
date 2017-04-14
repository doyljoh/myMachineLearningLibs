# -*- coding: utf-8 -*-
"""
Perform ETL operations to perpare the data for feature engineering modeling

Author: John Doyle
"""


import logging
import os
from ..utilities import utilities as util
from .ETL import ETL_func as etlFunc
from time import gmtime, strftime

log = logging.getLogger(__name__)


class ETL:

    def __init__(self, configFilePath):
        """
            Create object and set initial object parameters

            :param configFilePath: The full directory path and file name of the configuration file 
        """

        # load configuration file
        log.info("Start ETL Module")
        self.config = util.load_config_json(configFilePath,'ETL')
        log.info("{0}: ETL Configuration: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),self.config))

    def numer(self, dataPath):
        """
            Run the ETL logic for the numer.ai competition

            :param dataPath: The full data directory path 
        """

        log.info("{0}: Run Numer ETL".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

        # Split data in training data: separate into additional training-validation
        etlFunc.split_numer_datasets(os.path.join(dataPath, "training"), self.config)

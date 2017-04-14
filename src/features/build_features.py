# -*- coding: utf-8 -*-
"""
Build features from the Datasets and perpare the data for modeling

Author: John Doyle
"""


import logging
import os
from ..utilities import utilities as util
from .feature_engineering import FeatEng_func  as etlFunc
from time import gmtime, strftime

log = logging.getLogger(__name__)


class FE:

    def __init__(self, configFilePath):
        """
            Create object and set initial object parameters

            :param configFilePath: The full directory path and file name of the configuration file 
        """

        # load configuration file
        log.info("Start FE Module")
        self.config = util.load_config_json(configFilePath,'FE')
        log.info("{0}: FE Configuration: {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),self.config))

    def numer(self, dataPath):
        """
            Run the Feature Extraction logic for the numer.ai competition

            :param dataPath: The full data directory path 
        """

        log.info("{0}: Run Numer FE".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

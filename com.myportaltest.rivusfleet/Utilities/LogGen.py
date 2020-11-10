'''
Created on 28 Oct 2020

@author: 612563313
'''

import logging


class LogGen():
    @staticmethod
    def logGen():
        logging.basicConfig(
                        filename=".\\Results\Logs\\LogGen.log",
                        format='%(asctime)s:%(levelname)s:%(message)',datefmt='%m/%d/%Y %I:%M:%S %p'
                        )
    
        logger = logging.getLogger()
        logger.setlevel(logging.INFO)
        return logger
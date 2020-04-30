#encoding:utf-8
import sys
sys.path.append("..")
from etc.setting_logger import LOGGING_DIC
import logging.config

class Log(object):
    @staticmethod
    def make_logger(name='default'):
        logger = logging.config.dictConfig(LOGGING_DIC)
        '''
        simple
        default
        common
        importance
        '''
        if name is not None:
            logger = logging.getLogger(name)
        return logger

if __name__ == '__main__':
    log = Log.make_logger()
    log.info('bbb')
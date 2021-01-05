import sys
sys.path.append("..")
from etc.setting_logger import LOGGING_DIC
import logging.config

class Log(object):
    @staticmethod
    def make_logger(name='default'):
        logger = logging.config.dictConfig(LOGGING_DIC)
        '''
        console:console
        default:console,common(info_xxxx.log),importance(err_xxxx.log)
        common:common(info_xxxx.log)
        importance:console,importance(err_xxxx.log)
        '''
        if name is not None:
            logger = logging.getLogger(name)
        return logger
        

     #def db(sql):
     #    pass


if __name__ == '__main__':
    log = Log.make_logger()
    log.info('bbbbbb')
    log.warning('cccccc')
    log.error('dddddd')
    log.critical('eeeeee')

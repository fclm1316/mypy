import time,os

timestr = time.strftime('%Y%m%d',time.localtime(time.time()))

standard_format='[%(levelname)s][%(asctime)s][%(threadName)s][%(thread)s]\
[%(filename)s:%(lineno)d][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s][%(lineno)d][%(message)s]'

id_simple_format = '[%(levelname)s][%(asctime)s][%(message)s]'

logfile_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../logs'))

logfile_info = ''.join('info_' + timestr + ".log")
logfile_err = ''.join('err_' + timestr + ".log")

LOGGING_DIC = {
                'version':1,
                'disable_existing_loggers':False,
                'formatters':{
                    'distinct':{
                        'format':standard_format
                        },
                    'simple':{
                        'format':simple_format
                    },
                    'less_simple':{
                        'format':id_simple_format
                    },
                },
                'filters':{},
                'handlers':{
                    'console':{
                        'level':'INFO',
                        'class':'logging.StreamHandler',
                        'formatter':'distinct',
                        },
                    'common':{
                        'level':'INFO',
                        'class':'logging.handlers.RotatingFileHandler',
                        'formatter':'simple',
                        'filename':'{}/{}'.format(logfile_path,logfile_info),
                        'maxBytes':1024*1024*100,
                        'backupCount':5,
                        'encoding':'utf-8',
                        },
                    'importance':{
                        'level':'ERROR',
                        'class':'logging.handlers.RotatingFileHandler',
                        'formatter':'distinct',
                        'filename':'{}/{}'.format(logfile_path,logfile_err),
                        'maxBytes':1024*1024*100,
                        'backupCount':5,
                        'encoding':'utf-8',
                    },
                 },
                 'loggers':{
                     'console':{
                            'handlers':['console'],
                            'level':'DEBUG',
                            'propagate':True,
                        },

                     'default':{
                            'handlers':['common','importance'],
                            'level':'INFO',
                            'propagate':True,
                        },

                     'common':{
                            'handlers':['common','console'],
                            'level':'INFO',
                            'propagate':True,
                        },
                        
                     'importance':{
                            'handlers':['console','importance'],
                            'level':'ERROR',
                            'propagate':True,
                        },
                    },

}

#print LOGGING_DIC

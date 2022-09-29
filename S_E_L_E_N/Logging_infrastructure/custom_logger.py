
import logging
import inspect

def customLogger(loglevel):
    
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    
    logger.setLevel(logging.DEBUG)
    
    fileHandler = logging.FileHandler('{0}.log'.format(loggerName), mode='w')
    fileHandler.setLevel(loglevel)
    
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M %p')
    
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    
    return logger
     
    

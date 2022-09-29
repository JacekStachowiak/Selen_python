import logging

class LoggerDemoConsole():
    
    def testLog(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)
        
        # create console
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)
        
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M %p')
        
        # add formatter to console czyli handler --> chandler
        chandler.setFormatter(formatter)
        
        # add handler to logger
        logger.addHandler(chandler)
        
        
        
demo = LoggerDemoConsole()
demo.testLog()        
        
from base.selen_driver import SelenDriver
import utilities.custom_logger as cl
import logging

class TestStatus(SelenDriver):
    
    log = cl.customLogger(logging.INFO)
    
    def __init__(self, driver):
        
        super(TestStatus, self).__init__(driver)
        self.resultlist = []
        
    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:  # nie musimy podawać is True
                    self.resultlist.append('PASS')
                    self.log.info(f'### VERYFICATION SUCCESSFULL ### :: {resultMessage}')  
                else:
                    self.resultlist.append('FAIL')     
                    self.log.error(f'### VERYFICATION FAIL ### :: {resultMessage}')
            else:
                self.resultlist.append('FAIL')     
                self.log.error(f'### VERYFICATION FAIL ### :: {resultMessage}')
        except:
            self.resultlist.append('FAIL')
            self.log.error('### Exception Occured !!!')
                                            
    
    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)
    
    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        
        if 'FAIL' in self.resultlist:
            self.log.error(f'{testName} ### TEST FAILED ###')
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(f'{testName} ### TEST  SUCCESSFULL ###')       
            self.resultlist.clear()    
            assert True == True 
            
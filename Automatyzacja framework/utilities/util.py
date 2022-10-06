import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util(object):
    
    log = cl.customLogger(logging.INFO)
    
    def sleep(self, sec, info=''):
        
        if info is not None:
            self.log.info(f'Wait :: {str(sec)} second for {info}')
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()
    
    def getAlphaNumeric(self, length, type='letters'):
        
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length)) 
    
    
    def getUniqueName(self, charCount=10):
        return self.getAlphaNumeric(charCount, 'lower')
    
    
    def getUniqueNameList(self, listSize=5, itemLenght=None):
        
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLenght[i]))
        return nameList
    
    
    def verifyTextContains(self, actualText, expectedText):
        
        self.log.info(f'Actual text from application Web UI --> :: {actualText}')                                               
        self.log.info(f'Expected text from application Web UI --> :: {expectedText}')        
        if expectedText.lower() in actualText.lower():
            self.log.info('### Verification Cantains ###')                                       
            return True
        else:
            self.log.info('### Verification does not Cantains !!!')
            return False
    
    
    def verifyTextMatch(self, actualText, expectedText):
        
        self.log.info(f'Actual text from application Web UI --> :: {actualText}')                                               
        self.log.info(f'Expected text from application Web UI --> :: {expectedText}') 
        if actualText.lower() == expectedText.lower():
            self.log.info('### Verification Matched ###')
            return True
        else:
            self.log.info('### Verification Does Not Matched ###')
            return False
    
    
    def verifyListMatch(self, expectedList, actualList):
        
        return set(expectedList) == set(actualList)
    
    
    def verifyListContains(self, expectedList, actualList):
        
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True           
            
            
        
            
            
        

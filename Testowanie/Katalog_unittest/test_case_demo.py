import unittest

class TestCaseDemo(unittest.TestCase):
    
    def setUp(self):
        print('Uruchamiam się przed każdym testem')
    
    def test_methodA(self):
        print('Uruchamiam metodę A')
    
    def test_methodB(self):
        print('Uruchamiam metodę B')          
    
    def tearDown(self):
        print('Uruchamiam się po wykonaniu wszystkich testów')  # czyszczenie wszystkiego co zainicjowano
    
if __name__ == '__main__':
    unittest.main(verbosity=2)    
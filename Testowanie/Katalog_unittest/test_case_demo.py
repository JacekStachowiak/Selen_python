import unittest

class TestCaseDemo(unittest.TestCase):
    
    @ classmethod
    def setUpClass(cls):
        print('#*' * 30)
        print('Uruchamiam się tylko raz przed wszystkimi testami - cls')
        print('#*' * 30)
        print()
        
    def setUp(self):
        print()
        print('Uruchamiam się przed każdym testem')
    
    def test_methodA(self):
        print('Uruchamiam metodę A')
    
    def test_methodB(self):
        print('Uruchamiam metodę B')          
    
    def tearDown(self):
        print('Uruchamiam się po wykonaniu każdego testu')  # czyszczenie wszystkiego co zainicjowano
    
    @ classmethod
    def tearDownClass(cls):
        print('#*' * 30)
        print('Uruchamiam się tylko raz po wszystkich testach - cls')
        print('#*' * 30)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)    
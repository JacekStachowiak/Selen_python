import unittest

class TestClass1(unittest.TestCase):
    
    @ classmethod
    def setUpClass(cls):
        print('#*' * 30)
        print('Class1 --> class level setUp - raz przed wszystkimi testami')
        print('#*' * 30)
        print()
        
    def setUp(self):
        print()
        print('Class1 --> setUp - przed każdym testem')
    
    def test_methodA(self):
        print('uruchamiam Class1 --> method A')
    
    def test_methodB(self):
        print('uruchamiam Class1 --> method B')          
    
    def tearDown(self):
        print('Class1 --> tearDown - po każdym teście')  
    
    @ classmethod
    def tearDownClass(cls):
        print('#*' * 30)
        print('Class1 --> class level tearDown - raz po wszystkich testach')
        print('#*' * 30)
        
if __name__ == '__main__':
    unittest.main(verbosity=2) 
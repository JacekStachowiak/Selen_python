import unittest

class TestClass1(unittest.TestCase):
    
    @ classmethod
    def setUpClass(cls):
        print('#*' * 30)
        print('Class1 --> class level setUp')
        print('#*' * 30)
        print()
        
    def setUp(self):
        print('Class1 --> setUp')
    
    def test_methodA(self):
        print('uruchamiam Class1 --> method A')
    
    def test_methodB(self):
        print('uruchamiam Class1 --> method B')          
    
    def tearDown(self):
        print('Class1 --> tearDown')  
    
    @ classmethod
    def tearDownClass(cls):
        print('#*' * 30)
        print('Class1 --> class level tearDown')
        print('#*' * 30)
        
if __name__ == '__main__':
    unittest.main(verbosity=2) 
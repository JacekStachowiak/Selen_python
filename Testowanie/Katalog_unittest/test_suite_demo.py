# tworzymy zestaw testowy/importujemy class-y z naszych plików testowych
import unittest
from test_class1 import TestClass1
from test_class2 import TestClass2

# get all tests from TestClass1 and TestClass2 - tworzymy zmienne
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# zestaw testowy łączący TestClass1/TestClass2
smoke_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
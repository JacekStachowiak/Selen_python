import pytest
from class_to_test import SomeClassToTest

@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class TestClassDemo():
    
    def test_methodA(self:
        print('Running method A')

    def test_methodB(self):
        print('Running method B')
        
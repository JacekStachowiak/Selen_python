import pytest
from class_to_test import SomeClassToTest

@pytest.mark.usefixtures('oneTimeSetUp','setUp')  # zamiast wpisywać do kolejnych method
class TestClassDemo():
    
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)  # wstawiam value
    
    def test_methodA(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 20
        print('Running method A')

    def test_methodB(self):         # nie wpisujemy do każdej method classSetup
        print('Running method B')
        
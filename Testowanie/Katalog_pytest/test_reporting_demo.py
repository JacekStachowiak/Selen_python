import pytest
from class_to_test import SomeClassToTest


# zamiast wpisywać do kolejnych method
@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print('Running method A')

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20          
        print('Running method B')

# py.test -s -v test_reporting_demo.py --browser firefox
# py.test -s -v test_reporting_demo.py --browser chrome
# py.test -s -v test_reporting_demo.py --browser chrome --html=htmlreport.html
# utworzył plik htmlreport.html
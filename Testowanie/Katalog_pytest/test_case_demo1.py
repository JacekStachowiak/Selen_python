import pytest
# uruchamiamy py.test
# py.test -v -s
# pliki tworzymy test_example.py lub example_test.py
# class name  TestExample
# test method test_example
# http://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/naming_conventions.html

# dopisuję do tych metod gdzie chcę np. tylko przed metodą A

@pytest.fixture
def setUp():    # nazwa dowolna
    print('Uruchamia się przed każdą method-ą')

def test_demo1_methodA(setUp):
    print('Uruchamiam demo1 metodę A')

def test_demo1_methodB(setUp):
    print('Uruchamiam demo1 metodę B')


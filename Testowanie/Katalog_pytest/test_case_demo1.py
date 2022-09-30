import pytest
# dopisuję do tych metod gdzie chcę np. tylko przed metodą A

@pytest.fixture
def setUp():    # nazwa dowolna
    print('Uruchamia się przed każdą method-ą')

def test_methodA(setUp):
    print('Uruchamiam metodę A')

def test_methodB():
    print('Uruchamiam metodę B')

# uruchamiamy py.test
# py.test -v -s

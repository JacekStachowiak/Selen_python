import pytest

@pytest.fixture()
def setUp():    
    print('Uruchamia się przed każdą method-ą')
    yield 
    print('Uruchamia się po każdej method-zie')

def test_demo2_methodA(setUp):
    print('Uruchamiam demo2 metodę A')

def test_demo2_methodB(setUp):
    print('Uruchamiam demo2 metodę B')

# py.test -s test_case_demo2.py    
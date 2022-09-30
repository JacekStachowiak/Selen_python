import pytest

@pytest.yield_fixture()
def setUp():    
    print('Uruchamia się przed każdą method-ą')
    yield 
    print('Uruchamia się po każdej method-zie')

def test_methodA(setUp):
    print('Uruchamiam metodę A')

def test_methodB(setUp):
    print('Uruchamiam metodę B')

# py.test -s test_case_demo2.py    
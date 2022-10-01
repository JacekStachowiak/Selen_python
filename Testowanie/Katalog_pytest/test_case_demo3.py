# py.test test_mod.py uruchamia test modul
# py.test somepath - uruchamia wszystkie testy w ścieżce
# py.test test_module.py::test_method   uruchamia konkretną method-ę w test module
# py.test -s test_case_demo2.py 
# py.test -s -v test_case_demo2.py  v - verbose

import pytest

@pytest.fixture()
def setUp():    
    print('Uruchamia demo3 setUp')
    yield 
    print('Uruchamia demo3 tearDown')

def test_demo3_methodA(setUp):
    print('Uruchamiam demo3 metodę A')

def test_demo3_methodB(setUp):
    print('Uruchamiam demo3 metodę B')
    
    
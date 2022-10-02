import pytest

@pytest.fixture()
def setUp():
    print('Uruchamiam method setUp')
    yield
    print('Uruchamiam method tearDown')
    
@pytest.fixture()
def oneTimeSetUp(scope='module'):
    print('Uruchamiam one time setUp')
    yield
    print('Uruchamiam one time tearDown')       
import pytest

@pytest.fixture()
def setUp():
    print('Uruchamiam conftest demo method setUp')
    yield
    print('Uruchamiam conftest demo method tearDown')
    
@pytest.fixture()
def oneTimeSetUp(scope='module'):
    print('Uruchamiam conftest demo one time setUp')
    yield
    print('Uruchamiam conftest demo one time tearDown')        
import pytest

@pytest.mark.parametrize('n',[1,2,3])
def test_5(n):
    print(n)
    print('test case 5')

@pytest.mark.M2
def test_6():
    print('test case 6')

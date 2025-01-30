import pytest
def test_3(setup):
    print('test case 3')

@pytest.mark.skip
def test_4():
    print('test case 4')
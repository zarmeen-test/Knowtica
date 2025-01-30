import pytest


def test_1(setup):
    obj1=setup
    obj1.get(r'https://demoapps.qspiders.com/')
    print('test case 1')

def test_2(setup):
    print('test case 2')
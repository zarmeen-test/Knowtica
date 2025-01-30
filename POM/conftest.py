import pytest

@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    drivers=webdriver.Chrome()
    drivers.implicitly_wait(10)
    drivers.get(r'https://practicetestautomation.com/practice-test-login/')
    drivers.maximize_window()
    time.sleep(2)
    yield drivers
    time.sleep(2)
    drivers.close()
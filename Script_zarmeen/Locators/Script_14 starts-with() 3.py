import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://www.python.org/')
drivers.maximize_window()
time.sleep(3)
drivers.find_elements( 'xpath','//a[starts-with(@href,"http")]')
time.sleep(2)
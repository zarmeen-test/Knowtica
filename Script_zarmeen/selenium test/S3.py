import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui?scenario=1')
drivers.maximize_window()
time.sleep(3)
drivers.find_element('xpath','//button[text()="Register"]')
time.sleep(2)
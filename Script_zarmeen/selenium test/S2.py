import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui?scenario=1')
drivers.maximize_window()
time.sleep(2)
drivers.find_elements('xpath','//a[starts-with(@href,"https")]')
time.sleep(2)
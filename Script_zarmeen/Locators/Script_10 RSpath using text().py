import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('xpath','//button[text()="Submit"]').click()
time.sleep(4)

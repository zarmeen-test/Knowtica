import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get('https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('class name','form-control').send_keys('syeda muizza')
time.sleep(2)
drivers.find_element('class name','form-control').send_keys('syeda@gmail.com')
time.sleep(4)

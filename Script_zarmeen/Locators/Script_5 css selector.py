import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('css selector','input#name').send_keys('syeda')
time.sleep(2)
drivers.find_element('css selector','textarea.form-control').send_keys('bangalore')
time.sleep(2)
drivers.find_element('css selector','input[id="email"]').send_keys('syeda@gmail.com')
time.sleep(2)
drivers.find_element('css selector','input.form-control[id="phone"]').send_keys('8296432698')
time.sleep(3)


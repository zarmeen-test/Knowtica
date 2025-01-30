import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui?scenario=1')
drivers.maximize_window()
time.sleep(1)
drivers.find_element('id','name').send_keys('syeda muizza')
time.sleep(2)
drivers.find_element('name','email').send_keys('syeda@gmail.com')
time.sleep(2)
drivers.find_element('name','password').send_keys('syeda123')
time.sleep(2)
drivers.find_elements()
#drivers.find_element('type','submit').click()
#drivers.find_element('xpath','//button[text()="Register"]').click()
drivers.find_element('xpath','//button[text()="Register"]').click()
time.sleep(12)


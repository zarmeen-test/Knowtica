import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui?scenario=1')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('xpath','//input[@id="name"]').send_keys('Muizza')
time.sleep(2)
drivers.find_element('xpath','//input[@id="email"]').send_keys('Muizza@gmail.com')
time.sleep(2)
drivers.find_element('xpath','//input[@id="password"]').send_keys('Muizza123')
time.sleep(2)
drivers.find_element('xpath','//button[@type="submit"]').click()
time.sleep(2)
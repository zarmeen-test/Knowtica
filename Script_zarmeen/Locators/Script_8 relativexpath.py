import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui?scenario=1')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('xpath','//*[@id="name"]').send_keys('Muizza')
time.sleep(2)
drivers.find_element('xpath','//*[@id="email"]').send_keys('Muizza@gmail.com')
time.sleep(2)
drivers.find_element('xpath','//*[@id="password"]').send_keys('Muizza123')
time.sleep(2)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article[1]/aside/article/aside[2]/div/div/form/div[4]/button').click()
time.sleep(2)


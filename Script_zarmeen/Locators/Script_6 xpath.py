import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui?scenario=1')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('xpath','/html/body/div/div/div[2]/section/main/section/article/aside/article/aside[2]/div/div/form/div/input').send_keys('syeda')
time.sleep(3)
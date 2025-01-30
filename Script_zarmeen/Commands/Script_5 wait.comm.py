import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui/progress/element?sublist=2')
drivers.maximize_window()
time.sleep(3)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section/section/input').send_keys(3)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/div[2]/button[1]').click()
time.sleep(10)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/section/select').click()
time.sleep(2)
import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(9)
drivers.get(r'https://demoapps.qspiders.com/ui/progress/element?sublist=2')
drivers.maximize_window()
time.sleep(2)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section/section/input').send_keys(7)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/div[2]/button[1]').click()
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/section/select').click()
time.sleep(3)
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui/progress/element?sublist=2')
drivers.maximize_window()
time.sleep(2)
explicit=WebDriverWait(drivers,10,ignored_exceptions=Exception,poll_frequency=2)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section/section/input').send_keys(6)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/div[2]/button[1]').click()
element=explicit.until(EC.presence_of_element_located(('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/section/select')))
element.click()
time.sleep(2)

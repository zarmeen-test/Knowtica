import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui')
drivers.maximize_window()
time.sleep(2)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/div/section/aside/div/ul/li[5]').click()
dis_ele=drivers.find_element('xpath','//*[@id="name"]')
drivers.execute_script('arguments[0].removeAttribute("disabled")',dis_ele)
dis_ele.send_keys('syeda')
time.sleep(2)
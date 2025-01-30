import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://demoapps.qspiders.com/ui/browser/newTab?sublist=1')
drivers.maximize_window()
time.sleep(3)
drivers.find_element('xpath','//*[@id="browserButton4"]').click()
time.sleep(2)
#drivers.quit()
drivers.close()
time.sleep(2)
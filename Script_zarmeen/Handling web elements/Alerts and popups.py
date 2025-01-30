import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(20)
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(2)
#simple alert
# drivers.find_element('xpath','//*[@id="alertBtn"]').click()
# simplealert=drivers.switch_to.alert
# time.sleep(2)
# simplealert.accept()
# time.sleep(2)
#confirmation alert
# drivers.find_element('xpath','//*[@id="confirmBtn"]').click()
# confalert=drivers.switch_to.alert
# time.sleep(2)
# # confalert.accept()
# confalert.dismiss()
# time.sleep(2)
#Prompt alert
drivers.find_element('xpath','//*[@id="promptBtn"]').click()
promalert=drivers.switch_to.alert
time.sleep(2)
promalert.send_keys('hey you')
promalert.accept()
time.sleep(5)
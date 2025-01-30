import time
from  selenium import webdriver
from selenium.webdriver.support.select import Select
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
drivers.get(r'https://demoapps.qspiders.com/ui/datePick/datedropdown?sublist=1')
drivers.maximize_window()
time.sleep(2)
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/article/div/div').click()
month=drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/article/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]')
while True:
    mon_year=month.text
    if mon_year=='December 2012':
        break
    else:
        drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/article/div/div[2]/div[2]/div/div/button[1]').click()
time.sleep(2)
dates=drivers.find_elements('xpath','//div[@role="option"]')
for i in dates:
    if i.text=='20':
        i.click()
        break
time.sleep(2)


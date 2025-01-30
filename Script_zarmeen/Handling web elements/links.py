import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(2)
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(3)
links=drivers.find_elements('xpath','//a')
for i in links:
    print(i.text)
for i in links:
    if i.text=="Youtube":
        i.click()
time.sleep(2)
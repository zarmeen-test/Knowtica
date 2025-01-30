import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(3)
element=drivers.find_element('xpath','//*[@id="name"]')
print(element.is_enabled())
print(element.is_displayed())
radiobutton=drivers.find_element('xpath','//*[@id="male"]')
print(radiobutton.is_selected())
radiobutton.click()
print(radiobutton.is_selected())
time.sleep(2)
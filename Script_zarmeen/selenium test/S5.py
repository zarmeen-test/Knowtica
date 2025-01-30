import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(2)
links=drivers.find_elements('tag name','a')
print(len(links))
radiobutton=drivers.find_elements('tag name','radio')
print(len(radiobutton))
checkboxes=drivers.find_elements('tag name','checkbox')
print(len(checkboxes))
time.sleep(2)

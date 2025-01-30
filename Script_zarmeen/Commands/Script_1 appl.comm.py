import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(3)
print(drivers.title)
print(drivers.current_url)
print(drivers.page_source)
time.sleep(2)

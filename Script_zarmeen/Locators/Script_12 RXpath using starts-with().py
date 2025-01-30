import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://www.python.org/')
drivers.maximize_window()
time.sleep(3)
links=drivers.find_elements('xpath','//a[starts-with(text(),"Python")]')
print(len(links))
time.sleep(2)
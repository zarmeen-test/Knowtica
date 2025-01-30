import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://www.online-python.com/')
drivers.maximize_window()
time.sleep(4)
links=drivers.find_elements('xpath','//a[contains(text(),"py")]')
print(len(links))
time.sleep(2)


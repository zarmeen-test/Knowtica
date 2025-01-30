import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://www.python.org/')
drivers.maximize_window()
time.sleep(3)
drivers.find_elements('xpath','//input[starts-with(@name,"user") and starts-with(@type,"text")]')
time.sleep(2)
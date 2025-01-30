import time
import requests
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(2)
links=drivers.find_elements('xpath','//a')
urls=[]
for i in links:
    if i.get_attribute('href')!=None:
        urls+=[i.get_attribute('href')]
for i in urls:
    response=requests.get(i)
    if response.status_code!=200:
        print(f'{i} is a broken link')
    else:
        print(f'{i} is not a broken link')
time.sleep(2)

import time
import Utilities
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
drivers.get(r'https://practicetestautomation.com/practice-test-login/')
drivers.maximize_window()
time.sleep(2)

path=r'C:\Users\zmuiz\OneDrive\Documents\DDT_data.xlsx'
rows=Utilities.row_count(path,'Sheet1')
for r in range(2,rows+1):
    UN=Utilities.read_data(path,'Sheet1',r,1)
    PWD=Utilities.read_data(path,'Sheet1',r,2)
    drivers.find_element('xpath','//*[@id="username"]').clear()
    drivers.find_element('xpath','//*[@id="username"]').send_keys(UN)
    time.sleep(2)
    drivers.find_element('xpath','//*[@id="password"]').clear()
    drivers.find_element('xpath','//*[@id="password"]').send_keys(PWD)
    time.sleep(2)
    drivers.find_element('xpath','//*[@id="submit"]').click()
    time.sleep(2)
    if drivers.title=='Logged In Successfully | Practice Test Automation':
        print('test passed')
        Utilities.write_data(path,'Sheet1',r,4,'passed')
        drivers.back()
    else:
        print('test failed')
        Utilities.write_data(path,'Sheet1',r,4,'failed')
    time.sleep(2)
time.sleep(2)
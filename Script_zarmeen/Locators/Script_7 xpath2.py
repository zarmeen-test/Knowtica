import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(4)
drivers.find_element('xpath','/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input[1]').send_keys('Muizza')
time.sleep(3) 
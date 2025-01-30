import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://www.amazon.in/?ref_=icp_country_from_us')
drivers.maximize_window()
time.sleep(4)
#to open mobile link using link text
drivers.find_element('link text','Mobiles').click()
time.sleep(3)
#to open electronics link using partial link text
drivers.find_element('partial link text','Elect').click()
time.sleep(3)

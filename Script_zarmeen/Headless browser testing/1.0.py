import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
obj=Options()
obj.add_argument('--headless')
# obj.add_experimental_option('detach',True)
# drivers=webdriver.Chrome(options=obj)
# drivers.get(r'https://demoapps.qspiders.com/ui')
# drivers.maximize_window()
# time.sleep(2)
# links=drivers.find_elements('xpath','//a')
# print(len(links))
time.sleep(2)


import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(20)
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(2)
drivers.switch_to.new_window('tab')
drivers.get(r'https://www.amazon.com/')
drivers.maximize_window()
time.sleep(2)
drivers.switch_to.new_window('tab')
drivers.get(r'https://www.myntra.com/')
drivers.maximize_window()
time.sleep(2)
drivers.switch_to.new_window('tab')
drivers.get(r'https://demoapps.qspiders.com/')
drivers.maximize_window()
time.sleep(2)
winID=drivers.window_handles
print(winID)
drivers.switch_to.window(winID[1])
drivers.close()
drivers.switch_to.window(winID[0])
drivers.close()
time.sleep(2)
winID=drivers.window_handles
for i in winID:
    drivers.switch_to.window(i)
    print(drivers.title)
time.sleep(2)


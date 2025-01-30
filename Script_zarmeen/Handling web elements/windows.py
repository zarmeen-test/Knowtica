import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(3)
drivers.find_element('xpath','//*[@id="HTML4"]/div[1]/button').click()
windowids=drivers.window_handles
#to print window ids
print(windowids)
##to close the particular window
# drivers.switch_to.window(windowids[1])
# time.sleep(3)
# drivers.close()
# time.sleep(3)
##to print the title of all opened windows
# parent=windowids[0]
# child=windowids[1]
# drivers.switch_to.window(parent)
# print(drivers.title)
# drivers.switch_to.window(child)
# print(drivers.title)
##the above operation can be done using for loop for multiple windows
# for id in windowids:
#     drivers.switch_to.window(id)
#     print(drivers.title)
##to open a new url in a fresh tab
# drivers.switch_to.new_window('tab')
# drivers.get(r'https://demoapps.qspiders.com/')
# time.sleep(3)
##to open a new url in a fresh window/browser
# drivers.switch_to.new_window('window')
# drivers.get(r'https://demoapps.qspiders.com/')
# time.sleep(3)





import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(2)
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(3)
checkboxes=drivers.find_elements('xpath','//input[@type="checkbox" and @class="form-check-input"]')
#to click on all checkboxes
# for i in checkboxes:
#     i.click()
#     time.sleep(1)
# #to click on all checkboxes in reverse order
# for i in checkboxes[::-1]:
#     i.click()
#     time.sleep(1)
#to click on first 3 checkboxes
# for i in checkboxes[:3:]:
#     i.click()
#     time.sleep(1)
# #to click on last 3 checkboxes
# for i in checkboxes[-1:-4:-1]:
#     i.click()
#     time.sleep(1)
#to click on a particular checkbox
for i in checkboxes:
    if i.get_attribute('id')=='monday' or i.get_attribute('id')=='saturday':
        i.click()
        time.sleep(1)
time.sleep(2)




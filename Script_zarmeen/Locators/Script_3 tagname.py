import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(4)
#to count the number of links
links=drivers.find_elements('tag name','a')
print(len(links))
#to count the number of images
images=drivers.find_elements('tag name','img')
print(len(images))
#to count the number of dropdowns
dropdowns=drivers.find_elements('tag name','select')
print(len(dropdowns))
#to count the number of table
tables=drivers.find_elements('tag name','table')
print(len(tables))
time.sleep(2)





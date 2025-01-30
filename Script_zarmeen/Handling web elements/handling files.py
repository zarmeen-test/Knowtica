import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
drivers.get(r'https://demoapps.qspiders.com/ui/fileUpload/multiple?sublist=3')
drivers.maximize_window()
time.sleep(2)
'''single file'''
# element=drivers.find_element('xpath','//*[@id="fileInput"]')
# element.send_keys(r'C:\Users\zmuiz\OneDrive\Desktop\api assignment.txt')
# time.sleep(2)
'''multiple files'''
element2=drivers.find_element('xpath','//*[@id="fileInput"]')
# element2.send_keys(r'C:\Users\zmuiz\OneDrive\Desktop\admin collection')
# element2.send_keys(r'C:\Users\zmuiz\OneDrive\Desktop\admin 1')
# time.sleep(2)
'''multiple files using for loop'''
files=[r'C:\Users\zmuiz\OneDrive\Desktop\admin collection', r'C:\Users\zmuiz\OneDrive\Desktop\admin 1']
for i in files:
    element2.send_keys(i)
    time.sleep(2)
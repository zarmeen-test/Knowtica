import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
# drivers.get(r'https://demoapps.qspiders.com/ui/scroll/newTabVertical')
drivers.get(r'https://demoapps.qspiders.com/ui/scroll/newHorizontal?scenario=1')
drivers.maximize_window()
time.sleep(2)
##vertical scroll down
'''top to bottom'''
# drivers.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# #to get pixel value
# pixel=drivers.execute_script("return window.pageYOffset;")
# print(pixel)
# time.sleep(2)
# '''bottom to top'''
# drivers.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# pixel2=drivers.execute_script("return window.pageYOffset;")
# print(pixel2)
# time.sleep(2)
# '''to scroll based on pixel'''
# drivers.execute_script("window.scrollBy(0,1500)")
# time.sleep(1)
# drivers.execute_script("window.scrollBy(0,-500)")
# time.sleep(1)
# drivers.execute_script("window.scrollBy(0,-1000)")
# time.sleep(3)
# '''to scroll upto particular element'''
# element=drivers.find_element('xpath','//*[@id="root"]/section/h1[3]')
# drivers.execute_script("arguments[0].scrollIntoView();",element)
# time.sleep(2)
##horizontal scroll down
drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section/a').click()
time.sleep(2)
windowids=drivers.window_handles
drivers.switch_to.window(windowids[1])
time.sleep(2)
drivers.execute_script("window.scrollBy(document.body.scrollWidth,0)")
time.sleep(2)
pixel=drivers.execute_script("return window.pageXOffset;")
print(pixel)
drivers.execute_script("window.scrollBy(-document.body.scrollWidth,0)")
time.sleep(2)
drivers.execute_script("window.scrollBy(3100,0)")
time.sleep(2)
drivers.execute_script("window.scrollBy(-3100,0)")
time.sleep(2)




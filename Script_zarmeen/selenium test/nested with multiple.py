import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
drivers.get(r'https://demoapps.qspiders.com/ui/frames/nestedWithMultiple?sublist=3')
drivers.maximize_window()
time.sleep(2)
frame1=drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/iframe')
drivers.switch_to.frame(frame1)
frame2=drivers.find_element('xpath','/html/body/div/div/section/div[2]/iframe')
drivers.switch_to.frame(frame2)
frame3=drivers.find_element('xpath','/html/body/div/div/form/div[1]/iframe')
drivers.switch_to.frame(frame3)
drivers.find_element('xpath','//*[@id="email"]').send_keys('syeda')
time.sleep(1)
drivers.switch_to.parent_frame()
frame4=drivers.find_element('xpath','/html/body/div/div/form/div[2]/iframe')
drivers.switch_to.frame(frame4)
drivers.find_element('xpath','//*[@id="password"]').send_keys('123')
time.sleep(1)
drivers.switch_to.parent_frame()
frame5=drivers.find_element('xpath','/html/body/div/div/form/div[3]/iframe')
drivers.switch_to.frame(frame5)
drivers.find_element('xpath','//*[@id="confirm"]').send_keys('123')
time.sleep(1)
drivers.switch_to.parent_frame()
frame6=drivers.find_element('xpath','/html/body/div/div/form/div[4]/iframe')
drivers.switch_to.frame(frame6)
drivers.find_element('xpath','//*[@id="submitButton"]').click()
time.sleep(2)
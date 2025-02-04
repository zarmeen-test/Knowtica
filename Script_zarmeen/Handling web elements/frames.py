import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
'''single frame'''
# drivers.get(r'https://demoapps.qspiders.com/ui/frames')
# drivers.maximize_window()
# frame1=drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/iframe')
# drivers.switch_to.frame(frame1)
# drivers.find_element('id','username').send_keys('sye')
# drivers.find_element('id','password').send_keys('123')
# time.sleep(4)
# drivers.find_element('id','submitButton').click()
# time.sleep(2)
'''nested frame'''
# drivers.get(r'https://demoapps.qspiders.com/ui/frames/nested?sublist=1')
# frame1=drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/iframe')
# drivers.switch_to.frame(frame1)
# frame2=drivers.find_element('xpath','/html/body/div/div/section/div[2]/iframe')
# drivers.switch_to.frame(frame2)
# drivers.maximize_window()
# drivers.find_element('id','email').send_keys('zar')
# drivers.find_element('id','password').send_keys('456')
# drivers.find_element('id','confirm-password').send_keys('456')
# time.sleep(3)
# drivers.find_element('xpath','//*[@id="submitButton"]').click()
# time.sleep(2)
'''multiple frames'''
drivers.get(r'https://demoapps.qspiders.com/ui/frames/multiple?sublist=2')
frame1=drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section[1]/div[1]/iframe')
drivers.switch_to.frame(frame1)
drivers.maximize_window()
drivers.find_element('xpath','//*[@id="email"]').send_keys('zza')
drivers.find_element('xpath','//*[@id="password"]').send_keys('789')
drivers.find_element('xpath','//*[@id="confirm-password"]').send_keys('789')
time.sleep(3)
drivers.find_element('xpath','//*[@id="submitButton"]').click()
time.sleep(2)
drivers.switch_to.default_content()
frame2=drivers.find_element('xpath','//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section[1]/div[2]/iframe')
drivers.switch_to.frame(frame2)
drivers.find_element('xpath','//*[@id="username"]').send_keys('meen')
drivers.find_element('xpath','//*[@id="password"]').send_keys('012')
time.sleep(3)
drivers.find_element('xpath','//*[@id="submitButton"]').click()
time.sleep(2)
'''nested with multiple in selenium test directory'''
try:
    import time
    from selenium import webdriver
    drivers=webdriver.Chrome()
    drivers.get(r'https://testautomationpractice.blogspot.com/')
    drivers.maximize_window()
    time.sleep(2)
    drivers.find_element('xpath','//*[@id="name"]').send_keys('selenium')
    drivers.find_element('xpath','*[@id="email"]').send_keys('sele@gmail.com')
    time.sleep(2)
except:
    drivers.save_screenshot(r'C:\Users\zmuiz\OneDrive\Pictures\Screenshots\image2.png')
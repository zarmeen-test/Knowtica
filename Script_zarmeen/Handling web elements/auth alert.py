import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
drivers.get(r'https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/')
drivers.maximize_window()
time.sleep(4)
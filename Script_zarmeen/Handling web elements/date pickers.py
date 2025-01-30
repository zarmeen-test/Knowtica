import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
drivers=webdriver.Chrome()
drivers.implicitly_wait(2)
drivers.get(r'https://www.dummyticket.com/dummy-ticket-for-visa-application/?_gl=1*gxlcus*_up*MQ..*_gs*MQ..&gclid=CjwKCAiA3ZC6BhBaEiwAeqfvygdYltnKlxKDIV63-fYUxWCa6KfLV5C6ARLcP73m8vSuUdJGCQxpWRoCrTYQAvD_BwE')
drivers.maximize_window()
time.sleep(2)
drivers.find_element('xpath','//*[@id="departon"]').click()
monn=drivers.find_element('xpath','//*[@id="ui-datepicker-div"]/div[1]/div/select[1]')
month=Select(monn)
yearr=drivers.find_element('xpath','//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')
year=Select(yearr)
time.sleep(2)
dates=drivers.find_elements('xpath','//a[@class="ui-state-default"]')
for i in dates:
    if i.text=='27':
        i.click()
        break
drivers.find_element('xpath','//*[@id="ui-datepicker-div"]/div[2]/button[2]').click()
time.sleep(2)
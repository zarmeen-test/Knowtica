import time
from selenium import webdriver
drivers=webdriver.Chrome()
drivers.implicitly_wait(20)
drivers.get(r'https://testautomationpractice.blogspot.com/')
drivers.maximize_window()
time.sleep(2)
# columns=drivers.find_elements("xpath","//table[@name='BookTable']/tbody/tr/th")
rows=drivers.find_elements("xpath","//table[@name='BookTable']/tbody/tr")
# print(len(columns),len(rows))
for r in range(2,len(rows)+1):
    # for c in range(1,len(columns)+1):
    #     data=drivers.find_element('xpath',f'//table[@name="BookTable"]/tbody/tr[{r}]/td[{c}]').text
    #     print(data,end=' ')
    # print()
#print books belonging to author amit using if cond
    # author=drivers.find_element('xpath',f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[2]').text
    # if author=="Amit":
    #     bookname=drivers.find_element('xpath',f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[1]').text
    #     print(bookname)
# #print the price of books learn selenium and master in selenium using if cond
      book=drivers.find_element('xpath',f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[1]').text
      if book=="Learn Selenium" or book=="Master In Selenium":
          price=drivers.find_element('xpath',f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[4]').text
          print(price)
time.sleep(3)
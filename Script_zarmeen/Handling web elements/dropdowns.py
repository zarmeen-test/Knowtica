import time
from select import select
from selenium import webdriver
from selenium.webdriver.support.select import Select
drivers=webdriver.Chrome()
drivers.implicitly_wait(10)
# drivers.get(r'https://testautomationpractice.blogspot.com/')
# drivers.maximize_window()
# time.sleep(2)
# dropdown=drivers.find_element('xpath','//*[@id="country"]')
# country=Select(dropdown)
# country.select_by_visible_text('India')
# time.sleep(2)
# country.select_by_index(3)
# time.sleep(2)
# country.select_by_value('australia')
# time.sleep(2)
# '''to print the countries'''
# values=country.options
# for i in values:
#     print(i.text)
'''for multiple dropdown'''
drivers.get(r'https://demoapps.qspiders.com/ui/dropdown/multiSelect?sublist=1')
drivers.maximize_window()
dropdown2=drivers.find_element('xpath','//*[@id="select-multiple-native"]')
country2=Select(dropdown2)
country2.select_by_value('Running Shoes')
time.sleep(1)
country2.select_by_index(1)
time.sleep(1)
country2.select_by_visible_text('Casual Pants')
time.sleep(1)
# country2.deselect_all()
# country2.deselect_by_value('Casual Pants')
# country2.deselect_by_index(1)
allcountries=country2.all_selected_options
for i in allcountries:
    print(i.text)
time.sleep(2)
country2.deselect_all()
time.sleep(2)








from pyjavaproperties import Properties
path=r'C:\Users\zmuiz\PycharmProjects\pythonProject\demo.properties'

#write_data
ob=Properties()
ob.setProperty('url','https://testautomationpractice.blogspot.com/')
ob.setProperty('name','selenium')
var=open(path,'w')
ob.store(var)

#read_data
ob=Properties()
var=open(path,'r')
ob.load(var)
print(ob.getProperty('url'))
print(ob.getProperty('name'))

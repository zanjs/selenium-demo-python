# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()  # 打开火狐浏览器

driver.get('http://test.admin.6city.com/login/login')  # 打开登陆界面

driver.find_element_by_id('Account').send_keys('julian')
driver.find_element_by_id('Password').send_keys('julian')

time.sleep(2)  # 浏览器加载需要时间

driver.find_element_by_class_name('btn-submit').click()
# driver.close()

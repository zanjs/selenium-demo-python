# -*- coding: utf-8 -*-
from selenium import webdriver
# from time import sleep
import time
import os.path


dir = os.path.dirname(os.path.abspath('.'))
chrome_driver_path = dir + '/tools/chromedriver.exe'

# driver = webdriver.Chrome()  # 打开火狐浏览器
driver = webdriver.Chrome()

driver.get('http://www.baidu.com')  # 打开百度界面

driver.find_element_by_id('kw').send_keys('zanjs')  # 在搜索框内输入想要搜索内容

time.sleep(2)  # 浏览器加载需要时间

driver.find_element_by_id('su').click()  # 搜索完成

# mobileEmulation = {'deviceName': 'Apple iPhone 4'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)
#
# driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
#
# driver.get('http://m.baidu.com')
#
# sleep(3)
driver.close()
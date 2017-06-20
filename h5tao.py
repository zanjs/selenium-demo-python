# coding=utf-8
"""h5 taobao """
from __future__ import unicode_literals

import sys
import json
from time import sleep
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')

mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

open_url = 'https://h5.m.taobao.com/mlapp/odetail.html?bizOrderId=9650199740993454'

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get(open_url)
driver.implicitly_wait(30)


def load_config():
    """
    load config.json
    """
    f = open("config.json")
    config = json.load(f)

    return config



def isElementExist(self,element):
    """
    该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    """
    flag=True
    browser=self.driver
    try:
        browser.find_element_by_css_selector(element)
        return flag
    
    except:
        flag=False
        return flag


def is_element_exist(element):
    """
    判断元素是否存在
    """

    flag = True
    try:
        driver.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag

def code_img():
    """
    iframe 判断
    """
    iframe = driver.find_element_by_tag_name("iframe")

    driver.switch_to_frame(iframe)

    code_image_container = is_element_exist('#J_CodeImageContainer')

    if code_image_container:
        print '出现验证码'
    else:
        print '出现登陆'
        driver.find_element_by_id("username").send_keys(user_name)
        driver.find_element_by_id("password").send_keys(user_pwd)
        driver.find_element_by_id("btn-submit").click()


flag = is_element_exist("iframe")

config_data = load_config()

print config_data
print config_data['users'][0]
print config_data['users'][0]['pwd']

user_name = config_data['users'][0]['name']
user_pwd = config_data['users'][0]['pwd']

if flag:
    print "找到 iframe"

    code_img()

    driver.switch_to.default_content()

else:
    print '未找到 iframe'
    driver.find_element_by_id('username').send_keys(user_name)



sleep(1300)

driver.close()

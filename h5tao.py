# coding=utf-8
from selenium import webdriver
#
driver = webdriver.Firefox()
#
driver.get('https://login.m.taobao.com/login.htm?ttid=h5%40iframe&tpl_redirect_url=https%3A%2F%2Fh5.m.taobao.com%2Fother%2Floginend.html%3Forigin%3Dhttps%253A%252F%252Fh5.m.taobao.com')\

def  isElementExist(element):
    flag = True
    browser = driver
    try:
        browser.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag

flag = isElementExist("iframe")

if flag:
    print("111")
    frame = driver.find_element_by_css_selector("iframe")

    driver.switch_to.frame(frame)

    driver.find_element_by_id("username").send_keys('蓝莓静静')


else:
    print("222")
    driver.find_element_by_id('username').send_keys("蓝莓静静")
# driver.close()

#
# driver.close()

# import unittest
#
# from selenium import webdriver


# class test1(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.baseurl = "http://www.xebest.com"
#
#     #        self.driver.maximize_window()
#
#     def dengLu(self):
#         browser = self.driver
#
#         browser.get(self.baseurl)
#
#         browser.find_element_by_link_text(u"请登录").click()
#         # 调用isElementExist方法，判断元素是否存在
#         flag = test1.isElementExist(self, "div.popup-content")
#
#         if flag:
#
#             browser.find_element_by_id("userName").send_keys("w74581@163.com")
#             browser.find_element_by_id("password").send_keys("w123456")
#             browser.find_element_by_id("imgLogin").click()
#             print(browser.switch_to_alert().text)
#             browser.switch_to_alert().accept()
#
#
#         else:
#             print("没有弹框")




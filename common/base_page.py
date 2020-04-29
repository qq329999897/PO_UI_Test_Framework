import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    # 浏览器操作封装 -- > 二次封装
    def open_url(self,url):
        self.driver.get( url )
        logger.info('打开url地址 %s '% url )

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s'%value)
        return value
    #.....

    #元素操作封装
    # element_info = {'element_name':'用户名输入框','locator_type':'xpath','locator_value':'//input[@name="account"]','timeout': 5 }
    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver , locator_timeout)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功'%element_info['element_name'])
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作'%element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s' %(element_info['element_name'],content))

    # selenium执行js
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)

    def delete_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)


    def delete_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)

    def update_element_attribute(self, element_info, attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");' %(attribute_name,attribute_value), element)




    #frame == > id/name   frame元素对象
#    思路一
    def switch_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

#   思路二
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_by_element(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

#   思路三
    def switch_to_frame(self, **element_dict): #  switch_to_frame(id='frameid')  element=element_info
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame( element_dict['id'] )
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)











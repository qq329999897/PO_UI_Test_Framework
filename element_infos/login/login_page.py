import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@name="account"]',
        #                           'timeout': 5}
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 4}
        # self.login_button = {'element_name': '登录按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 2}
        elements = ElementdataUtils('login').get_element_info('login_page')
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']
        self.bug_link = elements['bug_link']

    def click_bug_link(self,bug_title='2020-04-14'):
        self.bug_link = self.bug_link.locator_value%bug_title
        self.click(self.bug_link)

    def input_username(self,username): #方法 == 》控件的操作
        self.input( self.username_inputbox , username )

    def input_password(self,password):
        self.input( self.password_inputbox , password )

    def click_login(self):
        self.click( self.login_button )

if __name__=="__main__":
    driver = Browser().get_driver()
    login_page =  LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()



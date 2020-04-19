import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log_utils import logger

class MainPage(object):
    def __init__(self):
        login_page = LoginPage()
        login_page.input_username('test01')
        login_page.input_password('newdream123')
        login_page.click_login()
        self.driver = login_page.driver # 把login_page的对象转移到mainpage
        self.companyname_showbox = self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.myzone_menu = self.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.username_showspan = self.driver.find_element(By.XPATH,'//span[@class="user-name"]')

    def get_companyname(self):  # 获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        return value

    def goto_myzone(self):  # 进入我的地盘菜单
        self.myzone_menu.click()

    def goto_product(self):  # 进入产品菜单
        time.sleep(1)
        self.product_menu.click()

    def get_username(self):
        value = self.username_showspan.text
        logger.info('获取用户名成功，用户名是：' + str(value) )
        return value

if __name__=="__main__":
   main_page =  MainPage()
   main_page.goto_myzone()
   main_page.goto_product()
   username = main_page.get_username()
   print( username )



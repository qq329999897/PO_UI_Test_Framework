import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser
from actions.login_action import LoginAction

driver = Browser().get_driver()
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
main_page = LoginAction(driver).default_login()
value = main_page.get_username()
print(value)
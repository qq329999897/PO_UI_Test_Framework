import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = local_config.url

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()
        #测试用例失败截图

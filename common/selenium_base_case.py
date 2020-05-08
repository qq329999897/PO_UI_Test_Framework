import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config
from common.log_utils import logger

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('')
        logger.info('==============测试类开始执行=============')
        cls.url = local_config.url

    def setUp(self) -> None:
        logger.info('---------测试方法开始执行-----------')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        # 测试用例失败截图
        # if len(self._outcome.errors)>=1:
        #     self.base_page.screenshot_as_file()
        errors = self._outcome.errors
        for test,exc_info in errors:
            if exc_info:
                self.base_page.screenshot_as_file()
        self.base_page.close_tab()
        logger.info('---------测试方法执行完毕-----------')

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('==============测试类执行完毕=============')

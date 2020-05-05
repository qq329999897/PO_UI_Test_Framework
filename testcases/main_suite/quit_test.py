import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.config_utils import local_config

class QuitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_quit(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        quit_action = QuitAction( main_page.driver )
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual( actual_result.__contains__('用户登录'),True,'test_quit用例不通过' )

if __name__=='__main__':
    unittest.main()





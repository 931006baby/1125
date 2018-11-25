#输入用户名
#输入密码
#点击登录
import os,sys
sys.path.append(os.getcwd())
from Base.get_driver import get_driver
from Page.page_login import PageLogin


class TestLogin:
    def setup_class(self):
        self.login=PageLogin(get_driver())
    def teardown_class(self):
        self.login.driver.quit()

    def test_login(self,username="1820000333",pwd="123456"):
        self.login.page_username(username)
        self.login.page_pwd(pwd)
        self.login.page_click_btn()




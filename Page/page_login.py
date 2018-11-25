from selenium.webdriver.common.by import By

from Base.base import Base
loc_username = By.ID,'com.vcooline.aike:id/etxt_username'
loc_pwd = By.ID,'com.vcooline.aike:id/etxt_pwd'
loc_login_btn = By.ID,'com.vcooline.aike:id/btn_login'

class PageLogin(Base):

#输入用户名
    def page_username(self,text):
        self.base_input(loc_username, text)


#输入密码
    def page_pwd(self,text):
        self.base_input(loc_pwd, text)
#点击登录

    def page_click_btn(self):
        self.base_click_element(loc_login_btn)
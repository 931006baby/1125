"""
需求：打开页面，输入信息，点击登录

"""
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    #初始化函数
    def __init__(self,driver):
        self.driver=driver

    #查找元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # return WebDriverWait(self.driver,timeout,poll_frequency=poll).\
        #     until(lambda x:x.find_element(*loc))
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
    #输入

    def base_input(self,loc,text):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(text)
#===点击元素

    def base_click_element(self,loc):
        self.base_find_element(loc).click()




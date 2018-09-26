from common.base import Base
from selenium import webdriver
import unittest
from time import sleep

login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"

class LoginPage(Base):
    #定位登录
    loc_user = ("id","account")
    loc_pwd = ("name","password")
    loc_button = ("id","submit")
    loc_keep = ("id","keepLoginon")
    loc_forget_pwd = ("link text","忘记密码")

    def input_user(self,text=""):
        self.sendKeys(self.loc_user,text)

    def input_pwd(self,text=""):
        self.sendKeys(self.loc_pwd,text)

    def click_keep(self):
        self.sendKeys(self.loc_keep)

    def clivk_forget_pwd(self):
        self.click(self.loc_forget_pwd)

    def click_login_button(self):
        self.click(self.loc_button)

    # def get_login_name(self):
    #     user = self.get_text()

# if __name__ == '__main__':

    # unittest.main()
    # from time import sleep
    # driver = webdriver.Chrome()
    # login_page = LoginPage(driver)
    # driver.get(login_url)
    # login_page.input_user("admin")
    # login_page.input_pwd("123456")
    # login_page.click_login_button()
    # sleep(2)
    # driver.quit()









from time import sleep
from selenium import webdriver
from page.login_pages import LoginPage
import unittest

class loginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login = LoginPage(cls.driver)
        login_url =  "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
        cls.driver.get(login_url)

    def test_01(self):
        self.login.input_user("admin")
        self.login.input_pwd("123456")
        self.login.click_login_button()
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





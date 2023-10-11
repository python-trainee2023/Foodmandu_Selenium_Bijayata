import time
from pydoc import classname

from selenium.webdriver.common.by import By

from Pages.LoginPage import loginPage

from testCases.baseTest import baseTest


class TestLogin(baseTest):

    def __init__(self, driver):
        self.driver = driver

    def test_validlogin(self):

        loginpage = loginPage(self.driver)

        loginpage.Login("Shresthabijayata44@gmail.com", "me9843671841")

        # self.Login("Shresthabijayata44@gmail.com", "me9843671841")
import pytest
from selenium.webdriver.chrome import webdriver

from testCases.Home import HomePage

from Pages.loginPage import loginPage
from testCases.baseTest import baseTest
from Pages.SearchPage import SearchPage





class TestMainPage(baseTest):

    def __init__(self):
        self.driver = None

    def test_casesall(self):

        loginpage =loginPage(self.driver)

        loginpage.Login("Shresthabijayata44@gmail.com", "me9843671841")

        searchPage = SearchPage(self.driver)

        searchPage.searchRestaurant("le trio")







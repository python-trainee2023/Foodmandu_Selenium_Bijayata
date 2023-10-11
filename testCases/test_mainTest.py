import pytest
from selenium.webdriver.chrome import webdriver

from testCases.Home import HomePage

from Pages.LoginPage import LoginPage
from testCases.baseTest import baseTest
from Pages.SearchPage import SearchPage
from Pages.AddToCartPage import AddToCartPage





class TestMainPage(baseTest):
    def test_casesall(self):

        login_page =LoginPage(self.driver)

        login_page.login("Shresthabijayata44@gmail.com", "me9843671841")

        search_page = SearchPage(self.driver)

        search_page.searchRestaurant("le trio")

        add_to_cart_obj = AddToCartPage(self.driver)
        add_to_cart_obj.add_to_cart()









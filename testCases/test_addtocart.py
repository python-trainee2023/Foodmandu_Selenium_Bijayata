
from testCases.baseTest import baseTest

from Pages.AddToCartPage import AddToCartPage


class TestAddToCart(baseTest):
    def test_addToCart(self):
        add_to_cart_obj = AddToCartPage(self.driver)
        add_to_cart_obj.add_to_cart()
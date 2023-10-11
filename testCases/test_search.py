
from testCases.baseTest import baseTest
from Pages.SearchPage import SearchPage


class TestSearch(baseTest):
    def test_Search(self):

        search_page = SearchPage(self.driver)

        search_page.searchRestaurant("le trio")
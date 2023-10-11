import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:
    def __init__(self, driver):
        self.driver = driver



    def searchRestaurant(self , restName):

        search_text_input= self.driver.find_element(By.XPATH, '//*[@placeholder="Restaurant or Cuisine (leave it blank to browse all)"]')
        search_text_input.send_keys(restName)

        time.sleep(2)
        find_rest_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn--primary btn-lg btn-block']")

        find_rest_button.click()

        time.sleep(2)



        click_restaurant = self.driver.find_element(By.XPATH, "//div[@class='col-md-4 col-lg-4 spinner ng-scope']")
        click_restaurant.click()

        time.sleep(2)






#

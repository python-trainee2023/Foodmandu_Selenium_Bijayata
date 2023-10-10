import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:
    def __init__(self, driver):
        self.driver = driver



    def searchRestaurant(self , restName):

        searchTextInput= self.driver.find_element(By.XPATH, '//*[@placeholder="Restaurant or Cuisine (leave it blank to browse all)"]')
        searchTextInput.send_keys(restName)

        time.sleep(5)
        findRestButton = self.driver.find_element(By.XPATH, "//button[@class='btn btn--primary btn-lg btn-block']")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(findRestButton)).click()

        # findRestButton = self.driver.find_element(By.XPATH, '//button[contains(text(),"Find Restaurants")]')
        #
        findRestButton.click()

        time.sleep(5)



        clickRestaurant = self.driver.find_element(By.XPATH, "//div[@class='col-md-4 col-lg-4 spinner ng-scope']")
        clickRestaurant.click()

        time.sleep(5)






#

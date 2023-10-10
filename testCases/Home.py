from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def loginLink(self):
        loginLink = self.driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')
        loginLink.click()

    def search(self, searchKey):
        clicksearch = self.driver.find_element(By.XPATH, "//input[@type='text']")
        clicksearch.click()
        clicksearch.clear()
        clicksearch.send_keys(searchkey)
        presssearch = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        presssearch.click()

    def gotocart(self):
        clickcartbutton = self.driver.find_element(By.XPATH, "//li[@class='dropdown cart-dropdown']")
        clickcartbutton.click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def loginclick(self):
        loginbutton = self.driver.find_element(By.XPATH, "//a[@class='user-access profile-link register']")
        loginbutton.click()

    def search(self, searchkey):
        clicksearch = self.driver.find_element(By.XPATH, "//input[@type='text']")
        clicksearch.click()
        clicksearch.clear()
        clicksearch.send_keys(searchkey)
        presssearch = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        presssearch.click()

    def gotocart(self):
        clickcartbutton = self.driver.find_element(By.XPATH, "//li[@class='dropdown cart-dropdown']")
        clickcartbutton.click()
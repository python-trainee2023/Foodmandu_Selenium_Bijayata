import time

from selenium.webdriver.common.by import By


class loginPage:

    def __init__(self, driver):
        self.driver = driver


    def loginLink(self):
        loginLink = self.driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')

        loginLink.click()

    # def clickRememberMe(self):
    #
    #     rememberMeCheckbox = self.driver.find_element(By.ID, "agreement")
    #     rememberMeCheckbox.click()

    def Login(self, email, password):
        self.loginLink()

        Email = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[1]/input')
        Email.send_keys(email)
        #
        Password = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[2]/input')
        Password.send_keys(password)
        #

        # self.clickRememberMe()

        loginButton = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[4]/button')
        loginButton.click()

        # time.sleep(10)







    # def login(self, username, password):
    #
    #     inputusername = self.driver.find_element(By.ID, "Username")
    #     inputusername.send_keys(username)
    #     inputpassword = self.driver.find_element(By.ID, "Password")
    #     inputpassword.send_keys(password)
    #     loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
    #     loginbutton.click()
    #
    # def invalidlogintext(self):
    #     invalidtextmessage = self.driver.find_element(By.XPATH,"//div[@class='card-content white-text']//p").text
    #     print(invalidtextmessage)
import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    def loginLink(self):
        login_link = self.driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')

        login_link.click()

    # def clickRememberMe(self):
    #
    #     rememberMeCheckbox = self.driver.find_element(By.ID, "agreement")
    #     rememberMeCheckbox.click()

    def login(self, email, password):
        self.loginLink()

        email_input = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[1]/input')
        email_input.send_keys(email)
        #
        password_input = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[2]/input')
        password_input.send_keys(password)
        #

        # self.clickRememberMe()

        loginButton = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[4]/button')
        loginButton.click()

        # time.sleep(10)








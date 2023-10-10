from selenium.webdriver.common.by import By
from selenium import webdriver


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://foodmandu.com/")

    def Login(self, email, password):
            Email = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[1]/input')
            Email.send_keys(email)
            #
            Password = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[2]/input')
            Password.send_keys(password)
            #

            loginButton = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[4]/button')
            loginButton.click()

            login_error = self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/p').text

            if (login_error):
                print(f'error-----{login_error}')

    def teardown(self):
        self.driver.quit()

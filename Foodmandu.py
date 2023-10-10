import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from assignment1.basetest import BaseTest


class TestLoginPage(BaseTest):

    # def Signin(self):
    #     signupLink = self.driver.find_element(By.XPATH, '//a[contains(text(),"Signup")]')
    #     signupLink.click()
    #
    #     time.sleep(5)
    #     Firstname = self.driver.find_element(By.XPATH, '// *[ @ id = "modal-body"] / form[1] / div / div[1] / input')
    #     Firstname.send_keys("Bijayata")
    #
    #     Lastname = self.driver.find_element(By.XPATH, '// *[ @ id = "modal-body"] / form[1] / div / div[2] / input')
    #     Lastname.send_keys("Shrestha")
    #
    #     Email = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[3]/input')
    #     Email.send_keys("Shresthabijayata4@gmail.com")
    #     #
    #     Phone = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[4]/input')
    #     Phone.send_keys("9843671841")
    #     #
    #     Password = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[5]/input')
    #     Password.send_keys("123")
    #     #
    #     confirmPassword = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[6]/input')
    #     confirmPassword.send_keys("123")
    #
    #     # // *[ @ id = "recaptcha-anchor"] / div[1]
    #     time.sleep(10)
    #     clickCaptcha = self.driver.find_element(By.XPATH, ' // *[ @ id = "recaptcha-anchor"] / div[1]')
    #     clickCaptcha.click()
    #
    #     time.sleep(5)
    #     # // *[ @ id = "modal-body"] / form[1] / div / div[9] / button
    #
    #     signupButton = self.driver.find_element(By.XPATH,
    #                                             ' // *[ @ id = "modal-body"] / form[1] / div / div[9] / button')
    #     signupButton.click()

    def Login(self, email, password):


        Email = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[1]/input')
        Email.send_keys(email)
        #
        Password = self.driver.find_element(By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[2]/input')
        Password.send_keys(password)
        #

        loginButton = self.driver.find_element(By.XPATH,'//*[@id="modal-body"]/form[1]/div/div[4]/button')
        loginButton.click()

        login_error = self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/p').text

        if(login_error):
            print(f'error-----{login_error}')



    def test_login(self):

        # loginLink_Xpath = self.driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')
        # login_Link = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, loginLink_Xpath))
        # )
        # login_Link.click()


        loginLink = self.driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')
        loginLink.click()
        time.sleep(5)



        self.Login("Shresthabijayata44@gmail.com", "me9843671841" )




    def waitVisibility(self):

        wait = WebDriverWait(self, 10) # Wait for a maximum of 10 seconds
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Login")]')))

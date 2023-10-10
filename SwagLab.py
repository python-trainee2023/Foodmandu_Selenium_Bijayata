# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# # Initialize the WebDriver (provide the path to your ChromeDriver executable)
# driver = webdriver.Chrome()
#
# # Open the login page (replace 'your_login_url' with the actual URL)
# driver.get("https://www.saucedemo.com/")
#
# # Locate the username and password input fields by their HTML attributes (replace 'id' and 'password' with actual values)
# username_input = driver.find_element(by=id("user-name"))
# password_input = driver.find_element(by=id("password"))
#
# # Enter the username and password (replace 'your_username' and 'your_password' with actual credentials)
# username_input.send_keys("test123")
# password_input.send_keys("test")
#
# # Submit the form (replace 'login_button_id' with the actual ID or selector of the login button)
# login_button = driver.find_element_by_id("login-button")
# login_button.click()
#
# # Assert that you are on the expected page after successful login (replace 'expected_url' with the URL you expect to be redirected to)
# # assert driver.current_url == "expected_url"
#
# # Close the WebDriver
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    # def teardown(self):
    #     self.driver.quit()


class TestLoginPage(BaseTest):

    def test_login(self):
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
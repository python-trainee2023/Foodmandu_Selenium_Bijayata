import pytest
from selenium import webdriver



@pytest.fixture()
def basetestSetup(request):
    driver = webdriver.Chrome()
    driver.get("https://foodmandu.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()



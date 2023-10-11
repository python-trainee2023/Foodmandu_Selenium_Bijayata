import time

from selenium.webdriver.common.by import By


class AddToCartPage:



    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # add_button = (By.XPATH, "//h3[@id = 'L280686']")
        # time.sleep(3)

        click_item1 = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Bacon Potato Roll')]")
        click_item1.click()
        # increase item

        self.item_add_modal("First item added")

        click_item2 = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Bacon Prawn Roll')]")
        click_item2.click()
        # increase item

        self.item_add_modal("Second item added")

        click_item3 = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Buffalo Wings')]")
        click_item3.click()
        # increase item

        self.item_add_modal("Third item added")

        time.sleep(2)

        proceed_button = self.driver.find_element(By.XPATH, "//button[text()='Proceed to Checkout']")

        proceed_button.click()







    def item_add_modal(self, notes):

        note_input = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Add Notes']")
        note_input.clear()
        note_input.send_keys(notes)

        increase_item = self.driver.find_element(By.XPATH,"//span[@class = 'icomoon icon-add icomoon--green']")
        increase_item.click()
        increase_item.click()

        time.sleep(2)
        decrease_item = self.driver.find_element(By.XPATH, "//span[@class= 'icomoon icon-remove icomoon--green']")
        decrease_item.click()
        time.sleep(2)

        # item_note = (By.XPATH,"//textarea[@placeholder='Add Notes']")


        time.sleep(2)

        # update_bag = (By.CLASS_NAME, "btn btn--primary btn-block btn--add-to-cart")
        add_to_bag = self.driver.find_element(By.XPATH,"//button[@class='btn btn--primary btn-block btn--add-to-cart']")

        add_to_bag.click()

        time.sleep(2)


    def show_item_details(self):
        sub_total = self.driver.find_element(By.XPATH,"//div[@class = 'cart__summary']//span")






















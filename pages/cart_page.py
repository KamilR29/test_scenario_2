from selenium.webdriver.common.by import By
from utils import wait
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from pages.place_order_modal import PlaceOrderModal


class CartPage(BasePage):


    CART_ROWS = (By.CSS_SELECTOR, "#tbodyid tr")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Place Order']")
    TOTAL_PRICE = (By.ID, "totalp")

    def is_loaded(self) -> bool:
        wait(self.driver, 10).until(EC.visibility_of_element_located(self.CART_ROWS))
        return True

    def get_product_names(self):
        rows = wait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.CART_ROWS))
        names = []
        for row in rows:
            name = row.find_element(By.XPATH, "./td[2]").text
            names.append(name)
        return names

    def has_product(self, product_name: str) -> bool:
        return product_name in self.get_product_names()

    def remove_product(self, product_name: str):
        rows = wait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.CART_ROWS))
        for row in rows:
            name = row.find_element(By.XPATH, "./td[2]").text
            if name == product_name:
                delete_btn = row.find_element(By.LINK_TEXT, "Delete")
                delete_btn.click()
                break
    def get_total_price(self) -> int:
        text = self.wait_for_visible(self.TOTAL_PRICE).text
        return int(text)

    def open_place_order(self):
        self.click(self.PLACE_ORDER_BTN)

    def open_place_order(self) -> PlaceOrderModal:
        self.click(self.PLACE_ORDER_BTN)
        return PlaceOrderModal(self.driver)


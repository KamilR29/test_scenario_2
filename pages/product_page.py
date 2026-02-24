from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#tbodyid h2")
    ADD_TO_CART_BTN = (By.LINK_TEXT, "Add to cart")

    def is_loaded(self) -> bool:
        self.wait_for_visible(self.PRODUCT_TITLE, timeout=10)
        return True

    def add_to_cart(self) -> str:
        self.is_loaded()
        self.click(self.ADD_TO_CART_BTN)
        return self.accept_alert_and_get_text()
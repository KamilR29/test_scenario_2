from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from utils import wait


class PlaceOrderModal(BasePage):

    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")

    PURCHASE_BTN = (By.XPATH, "//button[text()='Purchase']")

    SUCCESS_BOX = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    SUCCESS_TEXT = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible h2")
    SUCCESS_OK_BTN = (By.XPATH, "//button[text()='OK']")

    def is_loaded(self) -> bool:
        self.wait_for_visible(self.NAME_INPUT, timeout=10)
        return True

    def purchase(self, name, country, city, card, month, year) -> str:
        self.type(self.NAME_INPUT,name)
        self.type(self.COUNTRY_INPUT,country)
        self.type(self.CITY_INPUT,city)
        self.type(self.CARD_INPUT,card)
        self.type(self.MONTH_INPUT,month)
        self.type(self.YEAR_INPUT,year)

        self.click(self.PURCHASE_BTN)

        wait(self.driver, 10).until(EC.visibility_of_element_located(self.SUCCESS_BOX))
        return self.wait_for_visible(self.SUCCESS_TEXT).text

    def close_success(self):
        self.click(self.SUCCESS_OK_BTN)

from pages import BasePage
from selenium.webdriver.common.by import By


class ContactModal(BasePage):

    CONTACT_EMAIL = (By.ID,"recipient-email")
    CONTACT_NAME = (By.ID,"recipient-name")
    MESSAGE = (By.ID,"message-text")
    SEND_BTN = (By.XPATH, "//button[text()='Send message']")

    def send_message(self, contact_email: str, contact_name: str, message: str) -> str:
        self.type(self.CONTACT_EMAIL, contact_email)
        self.type(self.CONTACT_NAME, contact_name)
        self.type(self.MESSAGE, message)
        self.click(self.SEND_BTN)

        return self.accept_alert_and_get_text()


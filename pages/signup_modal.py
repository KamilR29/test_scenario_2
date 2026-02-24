from selenium.webdriver.common.by import By

from pages import BasePage


class SignupModal(BasePage):

    USERNAME_INPUT = (By.ID, "sign-username")
    PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_BTN = (By.XPATH, "//button[text()='Sign up']")

    def signup(self, username: str, password: str) -> str:
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SIGNUP_BTN)

        return self.accept_alert_and_get_text()
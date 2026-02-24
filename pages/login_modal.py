from selenium.webdriver.common.by import By

from pages import BasePage


class LoginModal(BasePage):

    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BTN = (By.XPATH, "//button[text()='Log in']")

    def login(self, username : str, password :str):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)


from pages import BasePage
from selenium.webdriver.common.by import By
from pages.signup_modal import SignupModal
from pages.login_modal import LoginModal
from pages.contact_modal import ContactModal


class HomePage(BasePage):

    URL = "https://www.demoblaze.com/index.html"

    SIGNUP_BTN = (By.ID, "signin2")
    LOGIN_BTN = (By.ID, "login2")
    CONTACT_BTN = (By.LINK_TEXT, "Contact")
    CART_BTN = (By.ID, "cartur")
    LOGOUT_BTN = (By.ID, "logout2")
    WELCOME_LABEL = (By.ID, "nameofuser")
    HOME_LINK = (By.LINK_TEXT, "Home")

    def open_home(self):
        self.open(self.URL)

    def is_loaded(self) -> bool:
        self.wait_for_visible(self.LOGIN_BTN, timeout=10)
        return True

    def go_home(self):
        self.click(self.HOME_LINK)

    def open_signup(self):
        self.click(self.SIGNUP_BTN)

    def open_login(self):
        self.click(self.LOGIN_BTN)

    def open_contact(self):
        self.click(self.CONTACT_BTN)

    def go_to_cart(self):
        self.click(self.CART_BTN)

    def logout(self):
        self.click(self.LOGOUT_BTN)

    def get_welcome_text(self) -> str:
        return self.wait_for_visible(self.WELCOME_LABEL, timeout=10).text

    def open_signup(self) -> SignupModal:
        self.click(self.SIGNUP_BTN)
        return SignupModal(self.driver)

    def open_login(self) -> LoginModal:
        self.click(self.LOGIN_BTN)
        return LoginModal(self.driver)

    def is_user_logged_in(self, username: str) -> bool:
        text = self.get_welcome_text()
        return username.lower() in text.lower()

    def open_contact(self) -> ContactModal:
        self.click(self.CONTACT_BTN)
        return ContactModal(self.driver)

    def open_category(self, category_name: str):
        self.click((By.LINK_TEXT, category_name))

    def open_product(self, product_name: str):
        self.click((By.LINK_TEXT, product_name))

    def go_home(self):
        self.click(self.HOME_LINK)

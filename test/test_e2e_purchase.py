import unittest
from selenium import webdriver
import time

from pages import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils import wait


class TestE2EPurchase(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(5)
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()


    def test_signup(self):
        self.home.open_home()

        signup_modal = self.home.open_signup()

        username = f"user_{int(time.time())}"
        password = "Test1234"

        alert_text = signup_modal.signup(username, password)
        self.assertIn("Sign up successful", alert_text)

    def test_user_can_login(self):
        self.home.open_home()

        username = f"user_{int(time.time())}"
        password = "Test1234"

        signup_modal = self.home.open_signup()
        signup_modal.signup(username, password)

        login_modal = self.home.open_login()
        login_modal.login(username, password)

        self.assertTrue(self.home.is_user_logged_in(username))

    def test_user_can_contact_us(self):
        self.home.open_home()

        email = "test@test.com"
        name = "Test User"
        message = "Hello from automation"

        contact_modal = self.home.open_contact()
        alert_text = contact_modal.send_message(email,name,message)

        self.assertIn("Thanks for the message", alert_text)

    def test_add_macbook_air_to_cart(self):
        self.home.open_home()

        self.home.open_category("Laptops")
        self.home.open_product("MacBook air")

        product_page = ProductPage(self.driver)
        alert_text = product_page.add_to_cart()

        self.assertIn("Product added", alert_text)

    def test_add_monitors_to_cart(self):
        self.home.open_home()

        self.home.open_category("Monitors")
        self.home.open_product("Apple monitor 24")

        product_page = ProductPage(self.driver)

        alert_text = product_page.add_to_cart()
        self.assertIn("Product added", alert_text)

    def test_product_visible_in_the_cart(self):
        self.home.open_home()

        self.home.open_category("Laptops")
        self.home.open_product("MacBook air")

        ProductPage(self.driver).add_to_cart()

        self.home.go_to_cart()

        cart = CartPage(self.driver)
        self.assertTrue(cart.is_loaded())
        self.assertTrue(cart.has_product("MacBook air"))

    def test_remove_one_monitor_form_cart(self):
        self.home.open_home()

        self.home.open_category("Monitors")
        self.home.open_product("Apple monitor 24")

        for _ in range(2):
            ProductPage(self.driver).add_to_cart()

        self.home.go_to_cart()
        cart = CartPage(self.driver)
        self.assertTrue(cart.has_product("Apple monitor 24"))

        cart.remove_product("Apple monitor 24")
        wait(self.driver,5).until(lambda d: len(cart.get_product_names())>=1)

    def test_user_can_complete_purchase(self):
        self.home.open_home()

        self.home.open_category("Laptops")
        self.home.open_product("MacBook air")
        ProductPage(self.driver).add_to_cart()

        self.home.go_to_cart()
        cart = CartPage(self.driver)

        place_order = cart.open_place_order()
        self.assertTrue(place_order.is_loaded())

        success_text = place_order.purchase(
            name="Test User",
            country="Poland",
            city="Warsaw",
            card="123456789",
            month="12",
            year="2025"
        )

        self.assertIn("Thank you for your purchase!", success_text)
        place_order.close_success()

    def test_user_can_logout(self):
        self.home.open_home()

        username = f"user_{int(time.time())}"
        password = "Test1234"

        signup = self.home.open_signup()
        signup.signup(username, password)

        login_modal = self.home.open_login()
        login_modal.login(username, password)

        self.assertTrue(self.home.is_user_logged_in(username))

        self.home.logout()





if __name__ == '__main__':
    unittest.main()


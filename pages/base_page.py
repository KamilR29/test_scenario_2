from  utils import wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open (self, url: str):
        self.driver.get(url)

    def wait_for_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=10):
        self.wait_for_clickable(locator, timeout).click()

    def type(self,locator, text, timeout=10, clear = True):
        el = self.wait_for_visible(locator, timeout)
        if clear:
            el.clear()
        el.send_keys(text)

    def accept_alert_and_get_text(self, timeout=10) -> str:
        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text
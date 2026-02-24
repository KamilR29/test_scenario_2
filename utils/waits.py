from selenium.webdriver.support.wait import WebDriverWait


def wait(driver, timeout = 10):
    return WebDriverWait(driver, timeout)

from selenium.webdriver.common.by import By


class Storefront:

    def __init__(self, driver):
        self.driver = driver

    def click_signin(self):
        self.driver.webdriver.find_element(By.CSS_SELECTOR, "li.authorization-link").click()

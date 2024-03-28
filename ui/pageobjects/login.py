from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    def fill_registered_customers(self, email_address, password):

        self.driver.webdriver.find_element(By.CSS_SELECTOR, "#email").send_keys(email_address)
        self.driver.webdriver.find_element(By.CSS_SELECTOR, "#pass").send_keys(password)






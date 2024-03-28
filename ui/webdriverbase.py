import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseDriver:

    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_driver = ChromeDriverManager().install()
        self.webdriver = webdriver.Chrome(service=Service(chrome_driver, options=chrome_options))

    def navigate(self, url):
        if isinstance(url, str):
            self.webdriver.get(url)
        else:
            raise TypeError("URL must be a string.")

    def take_screenshot(self, test_name):
        current_time = datetime.datetime.now()
        date_string = current_time.strftime("_%m_%d_%Y_%H%M%S")
        file_name = test_name + date_string + '.png'
        self.webdriver.save_screenshot(file_name)

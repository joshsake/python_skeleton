import datetime
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()


class BaseDriver:

    def __init__(self):
        self.instance = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities(),
                                         executable_path='../chromedriver.exe')

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

    def take_screenshot(self, test_name):
        current_time = datetime.datetime.now()
        date_string = current_time.strftime("_%m_%d_%Y_%H%M%S")
        file_name = test_name + date_string + '.png'
        self.instance.save_screenshot(file_name)

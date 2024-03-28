import logging
import pytest

from pageobjects.login import Login
from pageobjects.main_storefront import Storefront

from webdriverbase import BaseDriver

logger = logging.getLogger()


class TestDemo:

    def setup_method(self):
        self.driver = BaseDriver()

        self.driver.navigate("https://magento.softwaretestingboard.com/")

    @pytest.mark.smoke
    def test_login(self):
        logger.info("Starting at main landing page and then opening login page")
        self.storefront = Storefront(self.driver)
        self.storefront.click_signin()

        self.login_page = Login(self.driver)
        self.login_page.fill_registered_customers("test@email.com", "password")

        self.driver.take_screenshot("test_login")

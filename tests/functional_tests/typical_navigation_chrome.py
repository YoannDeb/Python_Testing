from selenium import webdriver
from flask_testing import LiveServerTestCase
import time

from server import app
from tests import conftest
from tests.functional_tests import config


class TestLogin(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('tests.functional_tests.config')
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit

    def test_open_chrome_windows(self):
        # self.browser = webdriver.chrome('tests/functional_tests/chromedriver')
        # self.browser.get(self.live_server_url)
        # time.sleep(30)
        # self.browser.close()
        self.driver.get(self.get_server_url())
        assert self.driver.current_url == 'http://localhost:8943/'

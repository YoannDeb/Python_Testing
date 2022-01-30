from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from . import typical_navigation_utils

PATH = "C:\\Program Files\\selenium_webdrivers\\geckodriver.exe"


def setup_firefox_webdriver():
    """
    Setup function for firefox webdriver using Selenium.
    Tries to use webdriver_manager to automatically download the webdriver.
    If it fails (Internet problem or Github API limit reached) it uses a manually downloaded driver
    located with PATH constant.
    :return: the driver object to be used in test function
    """
    try:
        service = Service(executable_path=GeckoDriverManager().install())
    except ValueError:
        service = Service(executable_path=PATH)
    options = FirefoxOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def test_typical_navigation():
    """
    Functional test function with Firefox.
    Uses setup_firefox_webdriver function to configure the driver.
    Uses typical_navigation function from typical_navigation_utils module to perform the test with Selenium.
    """
    driver = setup_firefox_webdriver()
    typical_navigation_utils.typical_navigation(driver)

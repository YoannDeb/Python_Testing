from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from . import typical_navigation_utils

PATH = "C:\\Program Files\\selenium_webdrivers\\chromedriver.exe"


def setup_chrome_webdriver():
    """
    Setup function for Chrome webdriver using Selenium.
    Tries to use webdriver_manager to automatically download the webdriver.
    If it fails (Internet problem or GitHub API limit reached) it uses a manually downloaded driver
    located with PATH constant.
    :return: the driver object to be used in test function
    """
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except ValueError:
        service = Service(executable_path=PATH)
    options = ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def test_typical_navigation():
    """
    Functional test function with Chrome browser.
    Uses setup_chrome_webdriver function to configure the driver.
    Uses typical_navigation function from typical_navigation_utils module to perform the test with Selenium.
    """
    driver = setup_chrome_webdriver()
    typical_navigation_utils.typical_navigation(driver)

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from . import typical_navigation_utils

PATH = "C:\\Program Files\\selenium_webdrivers\\geckodriver.exe"

def setup_firefox_webdriver():
    try:
        service = Service(executable_path=GeckoDriverManager().install())
    except ValueError:
        service = Service(executable_path=PATH)
    options = FirefoxOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def test_typical_navigation():
    driver = setup_firefox_webdriver()
    typical_navigation_utils.typical_navigation(driver)

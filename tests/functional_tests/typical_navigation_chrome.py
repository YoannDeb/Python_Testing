from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from . import typical_navigation_utils


def setup_chrome_webdriver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def test_typical_navigation():
    driver = setup_chrome_webdriver()
    typical_navigation_utils.typical_navigation(driver)

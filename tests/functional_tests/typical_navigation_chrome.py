from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
# from flask_testing import LiveServerTestCase
import time

# from server import app
# from tests import conftest
# from tests.functional_tests import config

# PATH = r"C:\Program Files (x86)\chromedriver.exe"


def setup_chrome_webdriver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# class TestLogin(LiveServerTestCase):
#
#     def create_app(self):
#         app.config.from_object('tests.functional_tests.config')
#         return app
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(PATH)
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test_open_chrome_windows(self):
#         self.browser = webdriver.Chrome('tests/functional_tests/chromedriver.exe')
#         self.browser.get(self.get_server_url())
#         time.sleep(30)
#         self.browser.close()
#     #     self.driver.get(self.get_server_url())
#     #     assert self.driver.current_url == 'http://localhost:8943/'

# def test_open_index():
#     driver = setup_chrome_webdriver()
#     driver.get("http://127.0.0.1:5000")
#     assert driver.title == "GUDLFT Registration"
#     # driver.implicitly_wait(1000)
#     time.sleep(10)
#     driver.quit()


def test_typical_navigation():
    driver = setup_chrome_webdriver()
    driver.maximize_window()
    driver.get('http://127.0.0.1:5000')
    time.sleep(5)
    points_chart_link = driver.find_element(By.LINK_TEXT, 'Points Chart')
    points_chart_link.click()
    time.sleep(5)
    back_to_index_link = driver.find_element(By.LINK_TEXT, 'Back to index')
    back_to_index_link.click()
    time.sleep(5)
    email_box = driver.find_element(By.NAME, 'email')
    enter_button = driver.find_element(By.TAG_NAME, 'button')
    email_box.send_keys("test@test.com")
    time.sleep(5)
    enter_button.click()
    time.sleep(5)
    email_box = driver.find_element(By.NAME, 'email')
    enter_button = driver.find_element(By.TAG_NAME, 'button')
    email_box.clear()
    email_box.send_keys("john@simplylift.co")
    time.sleep(5)
    enter_button.click()
    time.sleep(5)
    book_places_spring_festival_link = driver.find_element(By.LINK_TEXT, 'Book Places')
    book_places_spring_festival_link.click()
    time.sleep(10)
    places_box = driver.find_element(By.NAME, 'places')
    book_button = driver.find_element(By.TAG_NAME, 'button')
    places_box.send_keys("3")
    time.sleep(5)
    book_button.click()
    time.sleep(5)
    book_places_fall_classic_link = driver.find_elements(By.LINK_TEXT, 'Book Places')[1]
    book_places_fall_classic_link.click()
    time.sleep(5)
    logout_link = driver.find_element(By.LINK_TEXT, 'Logout')
    logout_link.click()
    time.sleep(5)
    driver.quit()

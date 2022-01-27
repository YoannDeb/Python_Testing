from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time


def setup_chrome_webdriver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


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

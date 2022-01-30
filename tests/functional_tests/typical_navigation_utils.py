from selenium.webdriver.common.by import By
import time

SLEEP_TIME = 5


def typical_navigation(driver):
    """
    Typical navigation function to use with any browser and powered by Selenium.
    Actions are:
    - Go to the index page
    - Click on the points chart link
    - Click on the back to index link
    - Fill the email form with non secretary email
    - Click on the send button
    - Fill the email form with a secretary email
    - Click on the send button
    - Click on the first festival's book places button
    - Book 3 places
    - Logout
    :param driver: driver configured for a specific browser.
    """
    driver.maximize_window()
    driver.get('http://127.0.0.1:5000')
    time.sleep(SLEEP_TIME)
    points_chart_link = driver.find_element(By.LINK_TEXT, 'Points Chart')
    points_chart_link.click()
    time.sleep(SLEEP_TIME)
    back_to_index_link = driver.find_element(By.LINK_TEXT, 'Back to index')
    back_to_index_link.click()
    time.sleep(SLEEP_TIME)
    email_box = driver.find_element(By.NAME, 'email')
    enter_button = driver.find_element(By.TAG_NAME, 'button')
    email_box.send_keys("test@test.com")
    time.sleep(SLEEP_TIME)
    enter_button.click()
    time.sleep(SLEEP_TIME)
    email_box = driver.find_element(By.NAME, 'email')
    enter_button = driver.find_element(By.TAG_NAME, 'button')
    email_box.clear()
    email_box.send_keys("john@simplylift.co")
    time.sleep(SLEEP_TIME)
    enter_button.click()
    time.sleep(SLEEP_TIME)
    book_places_spring_festival_link = driver.find_element(By.LINK_TEXT, 'Book Places')
    book_places_spring_festival_link.click()
    time.sleep(SLEEP_TIME)
    places_box = driver.find_element(By.NAME, 'places')
    book_button = driver.find_element(By.TAG_NAME, 'button')
    places_box.send_keys("3")
    time.sleep(SLEEP_TIME)
    book_button.click()
    time.sleep(SLEEP_TIME)
    book_places_fall_classic_link = driver.find_elements(By.LINK_TEXT, 'Book Places')[1]
    book_places_fall_classic_link.click()
    time.sleep(SLEEP_TIME)
    logout_link = driver.find_element(By.LINK_TEXT, 'Logout')
    logout_link.click()
    time.sleep(SLEEP_TIME)
    driver.quit()

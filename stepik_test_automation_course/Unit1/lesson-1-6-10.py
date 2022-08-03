from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import time

letters = string.ascii_uppercase
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    inputs = browser.find_elements(By.TAG_NAME, 'input')  # List of text fields
    for input in inputs:
        input.send_keys(''.join(random.choice(letters) for _ in range(8)))
        input.send_keys("random_word")

    button = browser.find_element(By.CSS_SELECTOR, " div button")
    time.sleep(10)  # waiting to visually evaluate the results of the script passing
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()
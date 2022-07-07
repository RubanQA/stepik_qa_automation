from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import time

letters = string.ascii_lowercase
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(''.join(random.choice(letters) for _ in range(8)))
        element.send_keys("random_word")

    button = browser.find_element(By.CSS_SELECTOR, "div .btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit()


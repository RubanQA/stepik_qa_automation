from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    labels = browser.find_elements(By.TAG_NAME,'label') # List of labels above text fields
    inputs = browser.find_elements(By.TAG_NAME, 'input') # List of text fields

    for i, label in enumerate(labels): # If the last character
        if label.text[-1] == '*': # of the label above the text field is equal to "*",
            inputs[i].send_keys('Required') # then in the input field we type "Required"

    button = browser.find_element(By.CSS_SELECTOR, " div button")
    time.sleep(10)  # waiting to visually evaluate the results of the script passing
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    num1 = int(num1.text)
    num2 = int(num2.text)
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(str(num1 + num2))
    send_button = browser.find_element_by_class_name("btn-default")
    send_button.click()

finally:
    time.sleep(5)
    browser.quit()
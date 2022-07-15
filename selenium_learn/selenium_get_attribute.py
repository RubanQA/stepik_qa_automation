from selenium import webdriver
import time
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


chest = browser.find_element_by_id("treasure")
x_value = chest.get_attribute("valuex")
result = calc(x_value)

input = browser.find_element_by_id("answer")
input.send_keys(result)
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobox = browser.find_element_by_id("robotsRule")
radiobox.click()
button = browser.find_element_by_class_name("btn-default")
time.sleep(5)
button.click()

browser.quit()


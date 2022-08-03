from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_number = browser.find_element_by_id("input_value")
x = x_number.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
button = browser.find_element_by_class_name("btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
radiobox = browser.find_element_by_id("robotsRule")
radiobox.click()
button.click()

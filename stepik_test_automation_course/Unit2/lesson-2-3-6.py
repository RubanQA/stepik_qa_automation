from selenium import webdriver
import time
import math

link1 = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link1)

button = browser.find_element_by_class_name("btn-primary")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_number = browser.find_element_by_id("input_value")
x = x_number.text
y = calc(x)
input = browser.find_element_by_id("answer")
input.send_keys(y)
button = browser.find_element_by_class_name("btn-primary")
button.click()

time.sleep(5)
browser.quit()

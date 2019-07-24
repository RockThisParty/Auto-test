import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(0.5)

input1 = browser.find_element_by_css_selector("div.first_block .form-group.first_class .first")
input1.send_keys("field one")

input2 = browser.find_element_by_css_selector("div.first_block .form-group.second_class .second")
input2.send_keys("Second field")

input3 = browser.find_element_by_css_selector("div.first_block .form-group.third_class .third")
input3.send_keys("Third field")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()
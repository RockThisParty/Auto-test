from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

#link = "http://suninjuly.github.io/file_input.html"
#browser = webdriver.Chrome()
#browser.get(link)

time.sleep(0.5)

'''
x_val = browser.find_element_by_id("treasure")
x = x_val.get_attribute("valuex")
fin_value =  math.log(abs(12*math.sin(int(x))))

answer = browser.find_element_by_id("answer")
answer.send_keys(str(fin_value))

checkbox = browser.find_element_by_css_selector("[type='checkbox']")
checkbox.click()

radibtn = browser.find_element_by_id("robotsRule")
radibtn.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

#browser.quit()
'''

'''
num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
sum = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))
'''

'''
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element_by_id("input_value").text
fin_value =  math.log(abs(12*math.sin(int(x))))

answer = browser.find_element_by_id("answer")
answer.send_keys(str(fin_value))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

browser.execute_script("window.scrollBy(0, 100);")

radiobtn = browser.find_element_by_id("robotsRule")
radiobtn.click()

button = browser.find_element_by_tag_name("button")
button.click()
'''

'''
browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements_by_class_name("form-control")
for element in elements:
	element.send_keys("Hakuna Matata")
	
cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, "debug.txt")

upload = browser.find_element_by_id("file")
upload.send_keys(file_path)
'''

'''
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value").text
result = math.log(abs(12*math.sin(int(x))))

answer = browser.find_element_by_id("answer")
answer.send_keys(str(result))
'''

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

book = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000'))
button = browser.find_element_by_id("book")
button.click()

x = browser.find_element_by_id("input_value").text
result = math.log(abs(12*math.sin(int(x))))

answer = browser.find_element_by_id("answer")
answer.send_keys(str(result))

button1 = browser.find_element_by_id("solve")
button1.click()

'''
button1 = browser.find_element_by_css_selector("button.trollface")
button1.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id("input_value").text
result = math.log(abs(12*math.sin(int(x))))

answer = browser.find_element_by_id("answer")
answer.send_keys(str(result))
'''

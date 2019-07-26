import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
	def test_registartion1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		browser.implicitly_wait(5)

		input1 = browser.find_element_by_css_selector("div.first_block .form-group.first_class .first")
		input1.send_keys("field one")

		input2 = browser.find_element_by_css_selector("div.first_block .form-group.second_class .second")
		input2.send_keys("Second field")

		input3 = browser.find_element_by_css_selector("div.first_block .form-group.third_class .third")
		input3.send_keys("Third field")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		browser.quit()
        
	def test_registartion2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		browser.implicitly_wait(5)

		input1 = browser.find_element_by_css_selector("div.first_block .form-group.first_class .first")
		input1.send_keys("field one")

		input2 = browser.find_element_by_css_selector("div.first_block .form-group.second_class .second")
		input2.send_keys("Second field")

		input3 = browser.find_element_by_css_selector("div.first_block .form-group.third_class .third")
		input3.send_keys("Third field")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		browser.quit()
        
if __name__ == "__main__":
    unittest.main()
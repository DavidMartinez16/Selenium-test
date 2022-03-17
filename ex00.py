from itertools import dropwhile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

s = Service("./drivers/geckodriver")
browser = webdriver.Firefox(service=s)
browser.implicitly_wait(20)

# Task 1
browser.get("https://www.amazon.com")
browser.find_element_by_id("twotabsearchtextbox").send_keys("Nike Shoes")
browser.find_element_by_id("nav-search-submit-button").click()
browser.back()
print('Title: %s' %browser.title)

# Task 2
browser.get("https://www.facebook.com")
browser.find_element_by_name("email").send_keys("jmartinezgualdron216@gmail.com")
browser.find_element_by_name("pass").send_keys("Dnvrek0216")
browser.find_element_by_name("login").click()


browser.quit()





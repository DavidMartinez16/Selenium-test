from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

firefoxOption = Options()
firefoxOption.add_argument("-headless")

s = Service("./drivers/geckodriver")
browser = webdriver.Firefox(service=s, options=firefoxOption)
#browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.get('https://www.linuxhint.com')
print('Title: %s' %browser.title)
browser.quit()


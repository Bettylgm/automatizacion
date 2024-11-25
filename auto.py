from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("https://www.google.com/")
driver.save_screenshot('screenshot_name.png')


Web_element = driver.find_element(By.NAME, 'q')
Web_element.send_keys ("selenium Webdriver" + Keys.ENTER)



time.sleep(30)



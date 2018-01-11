from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up Driver
driver = webdriver.PhantomJS()
driver.get("http://www.facebook.com/login")

# Log into Facebook
login = driver.find_element_by_css_selector('#email')
login.send_keys('YOUR-USERNAME-HERE')
password = driver.find_element_by_css_selector('#pass')
password.send_keys('YOUR-PASSWORD-HERE')
password.send_keys(Keys.RETURN)
time.sleep(2)

# Go to ad preferences
url = "https://www.facebook.com/ads/preferences/"
driver.get(url)
time.sleep(2)

# Click each like to remove

likes = driver.find_elements_by_css_selector('button[title]')
time.sleep(2)
for like in likes:
    like.click()
    time.sleep(2)

driver.quit()

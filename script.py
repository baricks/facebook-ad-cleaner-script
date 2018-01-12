from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# # Set up Driver
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Firefox()
driver.get("http://www.facebook.com/login")

# Log into Facebook
login = driver.find_element_by_css_selector('#email')
login.send_keys('YOUR-USERNAME')
password = driver.find_element_by_css_selector('#pass')
password.send_keys('YOUR-PASSWORD')
password.send_keys(Keys.RETURN)
time.sleep(2)

# Go to ad preferences
url = "https://www.facebook.com/ads/preferences/"
driver.get(url)
time.sleep(2)

# Your Interests
# Click each tab EXCEPT THE REMOVED INTERESTS TAB
tabs = driver.find_elements_by_class_name('_4xjz')
for idx, tab in enumerate(tabs):
    while idx < (enumerate(tabs)-1):
        tab.click()
        time.sleep(2)

    # Click each like to remove
    likes = driver.find_elements_by_css_selector('button[title]')
    for like in likes:
        like.click()
        time.sleep(2)

# Advertisements you've clicked on
ad_title = driver.find_element_by_class_name('_2qo7')
ad_title.click()
time.sleep(2)

# Click each ad tab
tabs = driver.find_elements_by_class_name('_4jq5')
for tab in tabs:
    tab.click()
    time.sleep(2)

    # Click each like to remove
    likes = driver.find_elements_by_css_selector('button[title]')
    for like in likes:
        like.click()
        time.sleep(2)

driver.quit()

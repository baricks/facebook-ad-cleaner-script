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
login.send_keys('USERNAME')
password = driver.find_element_by_css_selector('#pass')
password.send_keys('PASSWORD')
password.send_keys(Keys.RETURN)
time.sleep(2)

# Go to ad preferences
url = "https://www.facebook.com/ads/preferences/"
driver.get(url)
time.sleep(2)

# Your Interests
# Click each tab
tabs = driver.find_elements_by_class_name('_4xjz')
for tab in tabs[:-1]:
    try:
        tab.click()
        time.sleep(1)
    except:
        continue

    # Click each like to remove
    likes = driver.find_elements_by_css_selector('button[title]')
    for like in likes:
        try:
            like.click()
            time.sleep(1)
        except:
            continue

titles = driver.find_elements_by_class_name('_2qo7')
# Advertisements you've clicked on
titles[1].click()
time.sleep(1)

# Click each tab
tabs = driver.find_elements_by_class_name('_4jq5')
for tab in tabs[:-1]:
    try:
        tab.click()
        time.sleep(2)
    except:
        continue

    # Click each like to remove
    likes = driver.find_elements_by_css_selector('button[title]')
    for like in likes:
        try:
            like.click()
            time.sleep(2)
        except:
            continue

# Your information
titles[2].click()

# Click second tabs
tabs = driver.find_elements_by_class_name('_4jq5')
tabs[1].click()
# Click each category to remove
categories = driver.find_elements_by_class_name('_zom')
for category in categories:
    try:
        category.click()
        time.sleep(2)
    except:
        continue

driver.quit()

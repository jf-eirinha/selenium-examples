import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--lang=en-us")

# using Chrome to access the web
driver = webdriver.Chrome(options=options, 
	executable_path='C:/Users/joao_/Downloads/chromedriver_win32/chromedriver.exe')

# open the website
driver.get('https://www.stitcher.com')

# time for login (make it automatic!)
time.sleep(30)

# select the class
search_button = driver.find_element_by_class_name('searchButton')

# click the search button
search_button.click()

# select input box
input_box = driver.find_element_by_id('search')

# input the name of the podcast
podcast = input("What is the name of the podcast? ")

# send text to search
input_box.send_keys(podcast)

# click the search button again
search_button.click()

delay = 5

# search for list of results
try:
    search_results = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'showResultsList')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

print(search_results)

# search image
try:
    img = WebDriverWait(search_results, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

print(img)

# click image
img.click()

found = True

while found:

	try:
		load_more_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Load More Episodes')))
		load_more_button.click()
		print("Click")
	except TimeoutException:
		print ("You've reached the end OR page was still loading")

# os for file management
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# build tuple of (class, file) to turn in
submission_dir = 'trash'

dir_list = list(os.listdir(submission_dir))

for directory in dir_list:
	file_list = list(os.listdir(os.path.join(submission_dir, 
		directory)))
	if len(file_list) != 0:
		file_tup = (directory, file_list[0])

print(file_tup)

# using Chrome to access the web
driver = webdriver.Chrome('C:/Users/joao_/Downloads/chromedriver_win32/chromedriver.exe')

# open the website
driver.get('https://www.stitcher.com')

# select the class
search_button = driver.find_element_by_class_name('searchButton')

# click the search button
search_button.click()

# select input box
input_box = driver.find_element_by_id('search')

# send text to search
input_box.send_keys('freakonomics radio')

# click the search button again
search_button.click()
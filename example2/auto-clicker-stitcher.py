import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from absl import flags
from absl import app

# Web Driver options
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--lang=en-us")

# Flags
FLAGS = flags.FLAGS
flags.DEFINE_string('exe_path', 'C:/Users/Morty/Downloads/chromedriver_win32/chromedriver.exe', 'Path to Chrome Driver.')

def main(argv):

	# Initialize Web Driver
	driver = webdriver.Chrome(options=options, 
		executable_path=FLAGS.exe_path)

	# Open the website
	driver.get('https://www.stitcher.com')

	# Select button by class
	search_button = driver.find_element_by_class_name('searchButton')

	# Click the search button
	search_button.click()

	# Select input box
	input_box = driver.find_element_by_id('search')

	# Input the name of the podcast
	podcast = input("What is the name of the podcast? ")

	# Send text to search
	input_box.send_keys(podcast)

	# Click the search button again
	search_button.click()

	# Define page loading time delay
	delay = 5

	# Search for list of results
	try:
		search_results = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'showResultsList')))
		print ("Page is ready!")
	except TimeoutException:
		print ("Loading took too much time!")

	# Search podcast image
	try:
		img = WebDriverWait(search_results, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
		print ("Page is ready!")
	except TimeoutException:
		print ("Loading took too much time!")

	# Click image
	img.click()

	# Load more episodes loop
	found = True

	# Try/except to load click button each page reload
	while found:

		try:
			load_more_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Load More Episodes')))
			load_more_button.click()
			print("Click")
		except TimeoutException:
			print ("You've reached the end OR page was still loading")
			found = False

if __name__ == '__main__':
        app.run(main)

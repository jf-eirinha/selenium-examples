import pandas as pd
import csv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
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

        # Input IG url
        url = input('Input the url to the photo/video: ')

        # Open page
        driver.get(url)

        # Define page loading time delay
        delay = 10

        # Load more comments loop
        clickaroo = True

        # Try/except to load click button each page reload
        # On last comments it might show "View all XX comments" instead of "Load more comments"
        while clickaroo:

                try:
                        load_more_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((
                                By.XPATH, '//button[text()="Load more comments"]')))
                        ActionChains(driver).move_to_element(load_more_button).click(load_more_button).perform()
                        print("Loading more comments")
                except TimeoutException:
                        clickaroo = False

        try:
                load_more_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((
                By.XPATH, '//button[contains(text(), "View all")]')))
                ActionChains(driver).move_to_element(load_more_button).click(load_more_button).perform()    
        except TimeoutException:
                print ("Loaded all comments. In case the comments did not fully load try increasing delay.")

        # Find all comments
        menuitems = driver.find_elements_by_xpath('//li[@role="menuitem"]//span')

        comments = []

        # Add the webelement's text to list
        print('Creating list with comments')
        for menuitem in menuitems:
                comments.append(menuitem.text)

        # Convert list to pandas dataframe
        comments_df = pd.DataFrame(comments)

        # Write df to csv
        print('Saving comments to csv')
        comments_df.to_csv("ig-cmts.csv", index=False, header=False)

if __name__ == '__main__':
        app.run(main)

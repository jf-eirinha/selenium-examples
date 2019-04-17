# **Selenium Examples**

Here's two very basic examples of using Selenium in case you're doing some Data Science or Machine Learning project and quickly need to make a simple web scraper.

**Example 1: Instagram Comment Scraper 📷**

A basic scraper for Instagram comments. Takes a link to a photo or video and saves all comments to a .csv file. Maybe useful to get data for sentiment analysis for example. If you are interested you can look at ways to extend the script to extract all comments for one profile or hashtag.

![alt text](https://github.com/john-law/selenium-examples/blob/master/example1/example1.gif "Example 1 gif")

**Example 2: Stitcher Auto Clicker 🎶**

Are you trying to reach the end of a page but you're tired of clicking the "load more" button? Then this is the app for you! Stitcher does not allow you to order episodes from old to new on the web app so I use this so satisfy my OCD of always having to start at the oldest episode of a podcast.

**How to run**

1. Download ChromeDriver for your version of Chrome [here](http://chromedriver.chromium.org/downloads)
2. Install Selenium.

Using pip:

    pip install selenium
    
3. Run.

For Example 1:

    python ig-cmt-scraper.py --exe_path [/path_to_chrome_driver]

For Example 2:

    python stitcher-auto-clicker.py --exe_path [/path_to_chrome_driver]

4. After running user will be queried to input the IG page URL in Example 1 and the name of the podcast in Example 2. The .csv file is saved to /example1.

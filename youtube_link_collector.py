#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: Suresh

Source:
    page scroll refer below
    https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
'''

# Import necessary modules
 
from selenium import webdriver
import time
 
def get_yt_links(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path = 'C:\selenium_drivers\chromedriver.exe')

    driver.get(url)

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print('new_height['+str(new_height)+'], last_height['+str(last_height)+']')
            break
        last_height = new_height

    elems = driver.find_elements_by_xpath("//a[@href]")

    for elem in elems:
        print(elem.get_attribute("href"))


def startpy():
    #pass
    get_yt_links('https://www.youtube.com/channel/UCY6KjrDBN_tIRFT_QNqQbRQ/videos')


if __name__ == '__main__':
    startpy()
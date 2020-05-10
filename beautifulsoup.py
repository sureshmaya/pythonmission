#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# Import necessary modules
import requests
from bs4 import BeautifulSoup

def main():
    
    #print('Main')
    
    # Collect and parse first page
    page = requests.get('https://github.com/getify/BikechainJS')
    soup = BeautifulSoup(page.text, 'html.parser')    
    
    #print(soup)
    
    summary_element = soup.select("div.overall-summary")
    
    #print(summary_element)
    
    commits = summary_element[0].select("li.commits span.num")[0].text
    commits = str(commits).strip()
    print("commits : ", commits)
    
    repo_lang = summary_element[0].select("div.repository-lang-stats li a")

    for rl in repo_lang:
        lang = rl.select("span")[1].text
        lang = str(lang).strip()        
        
        lang_perc = rl.select("span")[2].text
        lang_perc = str(lang_perc).strip()
        
        print(lang, lang_perc)
        
        
if __name__ == '__main__':
    main()
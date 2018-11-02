# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:05:31 2018

@author: Phwong
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

start_url = 'https://www.hko.gov.hk/tide/ttext.htm'
prefix = 'https://www.hko.gov.hk/tide/'

def table_parser(soup):
    rows = soup.find_all('tr')[1:]
    for row in rows:
        cells = row.find_all('td')
        row_place = cells[0].text.replace('*', '').replace(' ', '_')
        links = cells[1].find_all('a')
        for link in links:
            get_table(prefix+link['href'],'highlow',row_place) #"{}_{}_{}.tsv".format('highlow',row_place,link.text))
        links = cells[2].find_all('a')
        for link in links:
            get_table(prefix+link['href'], 'hourly', row_place)    
               
def get_table(url, tide_type, row_place):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = [re.split(r"\s{3,}", line) for line in soup.find('pre').text.splitlines() if not line == "" if not '_' in line if not any(char.isalpha() for char in line)]
    if tide_type == 'highlow':
        pass
        #highlow_covert(pd.DataFrame(table))
    if tide_type == 'hourly':
        hourly_covert(pd.DataFrame(table))

# Convert the table format to three columns: date, time and tide
def hourly_covert(table):
    day_hour = range(1,24)

#def highlow_convert(table):
    
if __name__ == "__main__":
    soup = BeautifulSoup(requests.get(start_url).text, 'lxml')
    table_parser(soup)
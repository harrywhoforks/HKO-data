# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:05:31 2018

@author: Phwong
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url = 'https://www.hko.gov.hk/tide/ttext.htm'
prefix = 'https://www.hko.gov.hk/tide/'
high_low = 'high&low'
hourly = 'hourly'

def get_table_high_low(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('pre').text
    return table

def get_table_hourly(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('pre').text
    return table

if __name__ == "__main__":
    soup = BeautifulSoup(requests.get(start_url).text, 'lxml')
    rows = soup.find_all('tr')[1:]
    for row in rows:
        columns = row.find_all('td')
        row_name = columns[0].text.replace('*', '').replace(' ', '_')
        for column in columns[1:]:
            links = column.find_all('a')
            year = None
            for link in links:
                if link.text != year:
                    year = link.text
                    data = get_table_high_low(prefix+link['href'])
                elif link.text == year:
                    year = link.text
                    data = get_table_hourly(prefix+link['href'])
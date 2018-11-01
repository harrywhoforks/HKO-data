# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:05:31 2018

@author: Phwong
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

start_url = 'https://www.hko.gov.hk/tide/ttext.htm'
prefix = 'https://www.hko.gov.hk/tide/'

def get_table(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('pre').text
    with open(filename, 'w') as f:
        f.write(table)

if __name__ == "__main__":
    soup = BeautifulSoup(requests.get(start_url).text, 'lxml')
    rows = soup.find_all('tr')[1:]
    for row in rows:
        columns = row.find_all('td')
        row_name = columns[0].text.replace('*', '').replace(' ', '_')
        for column in columns[1:]:
            links = column.find_all('a')
            for link in links:
                get_table(prefix+link['href'], "{}_{}.tsv".format(row_name,link.text))

""" 
Scrapes some place that has an updated list of symbols. 
We choose 5 stocks to use with prices.py
"""

from bs4 import BeautifulSoup
import string
import requests


def get_all_stocks():
    # Get a current list of all the stock symbols for the NYSE
    # Create a list of every letter in the alphabet
    # Each page has a letter for all those symbols
    # i.e. http://eoddata.com/stocklist/NYSE/A.htm'
    alpha = list(string.ascii_uppercase)

    symbols = []

    # Loop through the letters in the alphabet to get the stocks on each page
    # from the table and store them in a list
    for each in alpha:
        url = 'http://eoddata.com/stocklist/NYSE/{}.htm'.format(each)
        resp = requests.get(url)
        site = resp.content
        soup = BeautifulSoup(site, 'html.parser')
        table = soup.find('table', {'class': 'quotes'})
        for row in table.findAll('tr')[1:]:
            symbols.append(row.findAll('td')[0].text.rstrip())       

    # Remove the extra letters on the end
    symbols_clean = []

    for each in symbols:
        each = each.replace('.', '-')
        symbols_clean.append((each.split('-')[0]))
    
    return symbols_clean


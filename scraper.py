""" 
Overview:
scraper.py includes:
- Methods to get lists of symbols from IEX

To-do:
- Hide API keys
- Add more functions to generate more subsets
"""

from bs4 import BeautifulSoup
import string
import requests
import urllib.request
import json

IEX_API_KEY = "pk_ddf96702d3cd4629b22432fffed5c330"


def get_all_stocks():
    """Gets a list of symbols for NYSE from an API

    Returns:
        [list] -- Returns a list of all symbols (strings) from the NYSE
    """
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


def get_top_gainers():
    """Gets list of top 10 gainers from API json response.

    Returns:
        [list] -- Returns a list of symbols (strings) of the top 10 gainers of the day.
    """
    symbols = []
    with urllib.request.urlopen("https://cloud.iexapis.com/stable/stock/market/list/gainers?token=" + IEX_API_KEY) as url:
        data = json.loads(url.read().decode())
        for obj in data:
            symbol = obj['symbol']
            symbols.append(symbol)
    return symbols


def get_top_losers():
    """Gets list of top 10 losers from API json response.

    Returns:
        [list] -- Returns a list of symbols (strings) of the top 10 losers of the day.
    """
    symbols = []
    with urllib.request.urlopen("https://cloud.iexapis.com/stable/stock/market/list/losers?token=" + IEX_API_KEY) as url:
        data = json.loads(url.read().decode())
        for obj in data:
            symbol = obj['symbol']
            symbols.append(symbol)
    return symbols

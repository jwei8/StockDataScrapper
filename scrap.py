import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

myStocks = ['AAPL', 'NUMI.V','GHIV']
stockData = []

def getData(symbol):
    headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

    url=f"https://ca.finance.yahoo.com/quote/{symbol}"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'symbol' : symbol,
    'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
    'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock

for item in myStocks:
    stockData.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json', 'w') as f:
    json.dump(stockData, f)

print('Fin.')

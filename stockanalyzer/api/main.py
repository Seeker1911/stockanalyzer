import os
import requests
import json
import pprint

def main():
  url = "https://www.alphavantage.co/query"

  function = "TIME_SERIES_DAILY"
  symbol = "AAPL"
  api_key = os.environ['ALPHA_VANTAGE_KEY']

  data = { "function": function, 
                   "symbol": symbol, 
                   "apikey": api_key } 
  page = requests.get(url, params = data)
  return page.json()

def iex():
  # https://api.iextrading.com/1.0/stock/aapl/batch?types=quote,news,chart&range=1m&last=10
  url = 'https://api.iextrading.com/1.0'
  ref_data = '/ref-data/symbols'
  stats = '/stats/intraday'
  stock = '/stock/aapl/batch' 
  type = '?types=quote,news,chart&range=1m&last=10'
  data = {'types': 'quote',
          'range': '1m'}
  url += stock
  page = requests.get(url, params = data)
  return page.json()

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
  #pprint.pprint(page.json())

import requests
from stockanalyzer.constants import *
from stockanalyzer.api.iex_utils import get_params, get_stock


def main():
  symbol = "AAPL"
  data = {"function": av_function_time_series_daily,
          "symbol": symbol, "apikey": api_key}
  page = requests.get(av_url, params=data)
  return page.json()

def iex():
  data = get_params('quote', '1m', '10')
  stock = get_stock('aapl')
  url = iex_url + stock
  page = requests.get(url, params=data)
  return page.json()

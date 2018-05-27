import requests
from stockanalyzer.constants import *
from stockanalyzer.api.iex_utils import get_params, get_stock
from stockanalyzer.api.av_utils import get_av_time_series_daily


def av():
  symbol = "AAPL"
  data = get_av_time_series_daily(symbol)
  page = requests.get(av_url, params=data)
  return page.json()


def iex():
  data = get_params('quote', '1m', '10')
  stock = get_stock('aapl')
  url = iex_url + stock
  page = requests.get(url, params=data)
  return page.json()

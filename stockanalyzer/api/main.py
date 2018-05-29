import requests
from stockanalyzer.constants import *
from stockanalyzer.api.iex_utils import get_params, get_stock
from stockanalyzer.api.av_utils import get_av_time_series_daily, parse_av_time_series_daily_data


def av():
  symbol = "AAPL"
  data = get_av_time_series_daily(symbol)
  page = requests.get(av_url, params=data)
  # data_set = parse_av_time_series_daily_data(page.json())
  # return data_set
  return page.json()


def iex():
  data = get_params('quote', '1m', '10')
  stock = get_stock('aapl')
  url = iex_url + stock
  page = requests.get(url, params=data)
  return page.json()

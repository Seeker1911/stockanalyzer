import os

iex_url = 'https://api.iextrading.com/1.0'
iex_ref_data = '/ref-data/symbols'
iex_stats = '/stats/intraday'

api_key = os.environ['ALPHA_VANTAGE_KEY']
av_url = 'https://www.alphavantage.co/query'
av_function_time_series_daily = 'TIME_SERIES_DAILY'
av_function_time_series_intraday = 'TIME_SERIES_INTRADAY'

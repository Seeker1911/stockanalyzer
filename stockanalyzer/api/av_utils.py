from stockanalyzer.constants import *


def get_av_time_series_daily(symbol):
    data = {'function': av_function_time_series_daily,
            'symbol': symbol,
            'apikey': api_key
            }
    return data

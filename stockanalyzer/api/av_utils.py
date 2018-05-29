import datetime as dt
from stockanalyzer.constants import *


def get_av_time_series_daily(symbol):
    """outputsize compact returns the last 100 data points. outputsize=full returns the entire data set up to 20 years.
        Switch to full when ready to train large data sets."""

    data = {'function': av_function_time_series_daily,
            'symbol': symbol,
            'apikey': api_key,
            'outputsize': 'compact'
            }
    return data


def parse_av_time_series_daily_data(page):
    meta_data = page['Meta Data']
    symbol = meta_data['2. Symbol']
    data = page['Time Series (Daily)']
    data_set = []
    for k, v in data.items():
        k = k.replace("'", '"')
        date = dt.datetime.strptime(k, '%Y-%m-%d')
        data_row = [symbol, date.date(), float(v['3. low']), float(v['2. high']),
                    float(v['4. close']), float(v['1. open'])]
        data_set.append(data_row)

    return data_set

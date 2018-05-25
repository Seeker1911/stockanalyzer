"""
The iex api does not require authentication. example rest call:
https://api.iextrading.com/1.0/stock/aapl/batch?types=quote,news,chart&range=1m&last=10
"""

def get_params(types, range, last):
  data = {'types': types,
          'range': str(range),
          'last': str(last)
          }
  return data

def get_stock(stock):
  params = '/stock/'+stock+'/batch'
  return params


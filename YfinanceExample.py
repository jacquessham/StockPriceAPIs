import pandas as pd
import yfinance
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from Graph import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Request data from yfinance
stock = yfinance.Ticker('0005.HK')
data = stock.history(period='max').reset_index()
data.to_csv('Results/HSBC_fulldataset_yf.csv', index=False)
fig = generate_candlestick(data['Date'], data['Open'],
                           data['Low'], data['High'], data['Close'],
	                       'Historical Stock Price of HSBC Holding (0005.HK)')
plotly.offline.plot(fig, filename='Results/HSBC_fulldataset_yf.html')

# Request data from yfinance with a day range
data = stock.history(period='ytd').reset_index()
data.to_csv('Results/HSBC_ytd_yf.csv', index=False)
fig = generate_candlestick(data['Date'], data['Open'],
                           data['Low'], data['High'], data['Close'],
	                       'Year-to-Date Stock Price of HSBC Holding (0005.HK)')
plotly.offline.plot(fig, filename='Results/HSBC_ytd_yf.html')

# Convert YTD stock price to be Normalized
data = stock.history(period='ytd').reset_index()
first_price = data.iloc[1,4] # Obtain the price of the first day of the period
data['Normalized'] = data['Close'].apply(lambda x: (x*1.0)/first_price)
data.to_csv('Results/HSBC_ytd_normalize_yf.csv', index=False)
fig = generate_line_chart(data['Date'], data['Normalized'],
	                       'Year-to-Date Normalized Stock Price ' + \
	                       'of HSBC Holding (0005.HK)''',
	                       'Index')
plotly.offline.plot(fig, filename='Results/HSBC_ytd_normalized_yf.html')
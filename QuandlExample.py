import pandas as pd
import quandl
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from Graph import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Quandl login
def getAPI(filepath):
	with open(filepath, 'r') as f:
		rawtext = f.read()
	textlist = rawtext.split(',')
	return textlist[1]

# Set API key first
quandl.ApiConfig.api_key = getAPI('../../License/QuandlAPIkey.csv')

# Request data from Quandl
data = quandl.get("HKEX/00005").reset_index()
data.to_csv('Results/HSBC_fulldataset_q.csv', index=False)
fig = generate_candlestick(data['Date'], data['Previous Close'],
                           data['Low'], data['High'], data['Nominal Price'],
	                       'Historical Stock Price of HSBC Holding (0005.HK)')
plotly.offline.plot(fig, filename='Results/HSBC_fulldataset_q.html')

# Request data from Quandl with a day range
start_date  = '2020-01-01'
end_date = '2020-05-07'
data = quandl.get("HKEX/00005", start_date=start_date,
	              end_date=end_date).reset_index()
data.to_csv('Results/HSBC_ytd_q.csv', index=False)
fig = generate_candlestick(data['Date'], data['Previous Close'],
                           data['Low'], data['High'], data['Nominal Price'],
	                       'Year-to-Date Stock Price of HSBC Holding (0005.HK)')
plotly.offline.plot(fig, filename='Results/HSBC_ytd_q.html')

# Request Preprocessed data from Quandl with a day range
data = quandl.get("HKEX/00005", start_date=start_date, end_date=end_date,
	              transformation="normalize").reset_index()
data.to_csv('Results/HSBC_ytd_normalize_q.csv', index=False)
fig = generate_line_chart(data['Date'], data['Nominal Price'],
	                       'Year-to-Date Normalized Stock Price ' + \
	                       'of HSBC Holding (0005.HK)''',
	                       'Index')
plotly.offline.plot(fig, filename='Results/HSBC_ytd_normalized_q.html')


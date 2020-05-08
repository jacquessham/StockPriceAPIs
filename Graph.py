import pandas as pd
import plotly.graph_objs as go


def generate_candlestick(date, open_price, low, high, close, title):
	data = [go.Candlestick(x=date, open=open_price, low=low, high=high,
	         close=close)]
	layout = {'title': title,
	          'xaxis':{'title':'Date','rangeslider':{'visible':False}},
			  'yaxis':{'title':'Price ($)'},
	          'hovermode':False}
	return {'data':data, 'layout':layout}

def generate_line_chart(x, y, title, yaxis_title):
	data = [{'x':x, 'y':y, 'mode':'lines'}]
	layout = {'title': title, 'xaxis':{'title':'Date'},
	          'yaxis':{'title': yaxis_title},
	          'hovermode':False}
	return {'data':data, 'layout':layout}
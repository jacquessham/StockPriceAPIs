# Stock Price APIs
The goal of this repository is to introduce free APIs to obtain financial data and stock price for various purpose. This repository also serves a supplemental role to my Medium Post, and you may find my post from <a href="">this link (Coming Soon)</a>.

## APIs to obtain Financial Data and Stock Price
<ul>
	<li>Quandl</li>
	<li>yfinance</li>
</ul>

## Files
There are 3 files in this repository:
<ul>
	<li>QuandlExample.py - Sample code to obtain data from Quandl</li>
	<li>YfinanceExample.py - Sample code to obtain data from yfinance</li>
	<li>Graph.py - Helper code to plot stock price with Plotly</li>
</ul>
<br>
The Results folder save the data in csv files and images of candlestick charts and line charts created from both <i>QuandlExample.py</i> and <i>YfinanceExample.py</i>. 

## Examples
In both example code, the code demostrates how to obtain stock price of HSBC Holding (0005.HK) traded in Hong Kong in 3 scenarios:
<ol>
	<li>Stock price with the maximum date range interval</li>
	<li>Stock price in year-to-date interval</li>
	<li>Normalize stock price in year-to-date interval</li>
</ol>
After the stock price is obtained, it would plot with candlestick chart or line chart with Plotly.

## Packages Needed
<ul>
	<li>pandas</li>
	<li>plotly</li>
	<li>quandl (For QuandlExample.py Only)</li>
	<li>yfinance (For YfinanceExample.py Only)</li>
</ul>

## Directions
Here is the direction to obtain data from either API after you have installed the package on your machine.

### Quandl
<ol>
	<li>Obtain Quandl code on the Quandl website, for HSBC Holdings (0005.HK), it is <i>HKEX/00005</i></li>
	<li>Import quandl</li>
	<li>Set API key to a quandl object</li>
	<li>Request data by calling .get() function from a quandl object. You may pass start date and end date to the .get() function. Also, you may pass a transformation type to .get()function if you want a transformed data set</li>
	<li>Quandl will return the stock price of HSBC Holdings in Pandas data frame.</li>
</ol>
<br>
The Quandl code must be found by searching the Quandl website.

### yfinance
<ol>
	<li>Import yfinance</li>
	<li>Request data by calling .Ticker() with a ticker from a yfinance object. Note that the ticker must be type in string with a Yahoo Finance accepted format. For HSBC Holdings (0005.HK), you will type <i>0005.HK</i>. It will return a object contains stock price with maximum available time interval from Yahoo Finance.</li>
	<li>To obtain stock price with a time interval, call .history() from the returned object with a time interval. You may entered a string of 3mo, 6mo, ytd, 1y, 5y...etc which represents 3 months, 6 months, year-to-date, 1 year, 5 years, representively. Transformed data is not available to yfinance, you have to do it with Pandas.</li>
	<li>Meta data or stock statistics may be obtained by calling .info() from the returned object, it returns a dictionary of meta data and statistics.</li>
</ol>
<br>
Yahoo Finance accepted format ticker is a standard format of ticker defined by Yahoo Finance. For US common stocks, the format is the same with either NYSE and Nasdaq. It has a rule for foreign stock tickers. For example, if you would like to obtain stock price traded in Hong Kong. The format is XXXX.HK, while you have to type the ticker in 4 digits, followed by <i>.HK</i>. It also has special format for US indexes. It is <i>^GSPC</i> for S&P 500 and <i>^DJI</i> for Dow Jones.
<br><br>
Note that there is a bug on calling <i>.info()</i>, to fix this, please uninstall yfinance and reinstall with <i></i>. See this <a href='https://github.com/ranaroussi/yfinance/issues/288'>post</a> for detail.

## Reference
<a href="https://docs.quandl.com/docs/python">Quandl Documentation</a>
<br>
<a href="https://pypi.org/project/yfinance/">yfinance Documentation</a>
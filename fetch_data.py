import yfinance as yf
import pandas as pd

def get_stock_data(symbol, period="5y"):
	"""
	Fetching historical stock data using yfinance.
	:param symbol" Stock icker symbol (e.g. "NVDA") 
	:param period: time range(default: "5y" for 5 years)
	:return: Pandas dataframe with Date and Close Price
	"""

	stock = yf.Ticker(symbol)
	df = stock.history(period=period)
	df = df[['Close']]    # keeping only closing price
	df.columns = ['close'] # Reaname for cosistency
	
	df = df.reset_index() #converting datetimeIndex to a column
	df['Date'] = pd.to_datetime(df['Date'])
	
	df['Date'] = df['Date'].astype(str)
	 
	return df 

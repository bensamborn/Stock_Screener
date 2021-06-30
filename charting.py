import pandas as pd  
import numpy as np 
import matplotlib as plt 

from priceData import timeSeries 

#Get data and clean data
ticker = 'AAPL'
tickData = timeSeries(ticker)
#filter 1Y
lookback = pd.DateOffset(days=365)
from datetime import time
import pandas as pd 
import requests 
from apiKey import getKey

def timeSeries(ticker_str):
    
    API_URL = "https://www.alphavantage.co/query"

    t_data = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": ticker_str,
        "outputsize": "full",
        "datatype": "json",
        "apikey": getKey()
        }

    response = requests.get(API_URL, t_data)
    response_json = response.json()

    data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index')
    
    data = data.reset_index()

    data.rename(columns={'index':'date','1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. adjusted close':'adj_close'},inplace=True)

    return data

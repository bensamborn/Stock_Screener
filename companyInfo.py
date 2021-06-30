import pandas as pd 
import requests 
from apiKey import getKey

def getOverview(ticker_str):
    
    API_URL = "https://www.alphavantage.co/query"

    t_data = {
        "function": "OVERVIEW",
        "symbol": ticker_str,
        "outputsize": "full",
        "datatype": "json",
        "apikey": getKey()
        }

    response = requests.get(API_URL, t_data)
    response_json = response.json()

    data = pd.DataFrame.from_dict(response_json, orient= 'index').sort_index(axis=1) 
    
    # Overview to data frame
    overviewTable = data
    stockDes = overviewTable.loc['Description',0]
    stockAddress = overviewTable.loc['Address',0]

    # Pull out company description and address
    overviewTable = overviewTable.drop('Description')
    overviewTable = overviewTable.drop('Address')

    overviewTable = overviewTable.rename(columns={0:'Equity Information'})

    return overviewTable,stockDes,stockAddress

def getIncome(ticker_str):
    
    API_URL = "https://www.alphavantage.co/query"

    #compact - first 100 lines
    #full - returns all 20 years of data

    t_data = {
        "function": "INCOME_STATEMENT",
        "symbol": ticker_str,
        "outputsize": "full",
        "datatype": "json",
        "apikey": getKey()
        }

    response = requests.get(API_URL, t_data)
    response_json = response.json() # maybe redundant

    data = pd.DataFrame.from_dict(response_json['annualReports']).sort_index(axis=1) 

    data = data.transpose()

    data = data.rename(columns={0:2020,1:2019,2:2018,3:2017,4:2016})

    return data

def getBalance(ticker_str):
    
    API_URL = "https://www.alphavantage.co/query"

    #compact - first 100 lines
    #full - returns all 20 years of data

    t_data = {
        "function": "BALANCE_SHEET",
        "symbol": ticker_str,
        "outputsize": "full",
        "datatype": "json",
        "apikey": getKey()
        }

    response = requests.get(API_URL, t_data)
    response_json = response.json() # maybe redundant

    data = pd.DataFrame.from_dict(response_json['annualReports']).sort_index(axis=1) 

    data = data.transpose()

    data = data.rename(columns={0:2020,1:2019,2:2018,3:2017,4:2016})

    return data
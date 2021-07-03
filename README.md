# Stock Screener - Powered by AlphaVantage
I developed this stock screener to gain experience with Flask and calling financial data from an API.

# Requirements
```
pip install pandas
pip install Flask
pip install datetime
```

# User Instructions
## Initialization
The WebApp is initialized by running main.py in a terminal or an IDE. Upon initialization, the user should go to [localhost:5000]((localhost:5000)) in their web browser of choice to use the appilcation. 
## Alpha Vantage Key
The user also needs to obtain their own Alpha Vantage API key to run the code successfully. An API key can be obtained at [alphavantage.co](https://www.alphavantage.co/support/#api-key) - the user will need to provide an email address to recieve a key.  

Upon receipt of a valid key, the user should replace the existing API key in apiKey.py.
```
def getKey():
    ### YOUR KEY HERE ###
    key = "L4W04J8F48N8J7OU"
    #####################
    return key
```
It is important to note that the Alpha Vantage API only allows for 5 calls/minute with a free key. The code will throw an exception if the limit is exceeded. 
# Interface
The home page is featured below:
![Home Page](/screenshots/home.PNG)
Search results of a valid ticker:
![Search Results](/screenshots/results.PNG)
# Improvements
1. The API key could be referenced as an environment variable 
2. The application could be deployed into the cloud or onto a server enironment in order to remove the need for user initialization 
3. Error handling could be added for invalid searches 
4. The templates could accept tables and variables as inputs as opposed to reading from and writing to a template on every click
5. The W3 CSS could be replaced with a more interesting CSS infrastucture 




import pandas as pd  
from flask import Flask, render_template, request
from datetime import datetime

from companyInfo import getOverview
from companyInfo import getIncome
from companyInfo import getBalance
from priceData import timeSeries

app = Flask(__name__)

# Make ticker search result global
global ticker

# Render index on startup and Home page
@app.route("/", methods =["GET", "POST"])
def index():

    return render_template('index.html')

@app.route("/Home",methods =["GET", "POST"])
def home():

    return render_template('index.html')

# Placeholder for about page / link to github
@app.route("/About")
def about():
    return render_template('index.html')

# Render overview dataframe for ticker 
@app.route("/Overview",methods =["GET", "POST"])
def Overview():

    global ticker

    if request.method == "POST":
        ticker = request.form.get("tname")
    
    navBar = open('templates\\navBar.html', 'r')
    navBar_text = navBar.read()
    navBar.close()

    sideBar = open('templates\\sideBar.html', 'r')
    sideBar_text = sideBar.read()
    sideBar.close()

    data = getOverview(ticker)
    tbl = data[0].to_html()
    des = str(data[1])
    IncAdd = str(data[2])

    f = open('templates\\overview.html', 'w')
    f.write(navBar_text)
    f.write(sideBar_text)
    # Write in company ticker, description, and address
    f.write('<h1>' + str(ticker) + '</h1>')
    f.write('<h2>' + des + '</h2>')
    f.write('<h3>Adress: ' + IncAdd + '</h3>')
    f.write(tbl)
    f.write('</div>')
    f.write('</body>')
    f.write('</html>')
    f.close()
    
    return render_template('overview.html')

@app.route("/PriceChart",methods =["GET", "POST"])
def chart():

    # Get price data
    legend = 'Price Data'
    data = timeSeries(ticker)
    data['date'] = pd.to_datetime(data['date'])
    data.sort_values(by=['date'],ascending=True,inplace=True)
    # Filter 1 Year
    tDate  = datetime.today()
    lookback = pd.DateOffset(days=365)
    fdate = tDate - lookback
    data = data[data['date'] >= fdate]
    # Send to chart js
    labels = data['date']
    values = data['adj_close']
    return render_template('chart.html', values=values, labels=labels, legend=legend, ticker=ticker)

# Function for Balance Sheet
@app.route("/BalanceSheet",methods =["GET", "POST"])
def balanceSheet():

    navBar = open('templates\\navBar.html', 'r')
    navBar_text = navBar.read()
    navBar.close()

    sideBar = open('templates\\sideBar.html', 'r')
    sideBar_text = sideBar.read()
    sideBar.close()

    data = getBalance(ticker)
    tbl = data.to_html()

    f = open('templates\\balanceSheet.html', 'w')
    f.write(navBar_text)
    f.write(sideBar_text)
    # Write in company ticker, description, and address
    f.write('<h1>' + str(ticker) + ' Balance Sheet</h1>')
    f.write(tbl)
    f.write('</div>')
    f.write('</body>')
    f.write('</html>')
    f.close()
    
    return render_template('balanceSheet.html')

# Function for Income Statement
@app.route("/IncomeStatement",methods =["GET", "POST"])
def incomeStatement():

    navBar = open('templates\\navBar.html', 'r')
    navBar_text = navBar.read()
    navBar.close()

    sideBar = open('templates\\sideBar.html', 'r')
    sideBar_text = sideBar.read()
    sideBar.close()

    data = getIncome(ticker)
    tbl = data.to_html()

    f = open('templates\\incomeStatement.html', 'w')
    f.write(navBar_text)
    f.write(sideBar_text)
    # Write in company ticker, description, and address
    f.write('<h1>' + str(ticker) + ' Income Statement</h1>')
    f.write(tbl)
    f.write('</div>')
    f.write('</body>')
    f.write('</html>')
    f.close()
    
    return render_template('incomeStatement.html')

if __name__ == "__main__":
    app.run(debug=True)
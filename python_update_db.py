import yfinance as yf
import pandas as pd
import psycopg2

# Download the list of companies in the S&P500
sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = sp500.Symbol.tolist()
# Define the columns we want to retrieve for each stock
cols = ['trailingPE', 'priceToBook', 'pegRatio']

# Download the stock data for all companies in the S&P500
stock_data = []
for ticker in tickers:
    try:
        info = yf.Ticker(ticker).info
        data = [ticker, info[cols[0]], info[cols[1]], info[cols[2]]]
        stock_data.append(data)
    except:
        pass

# Convert the stock data to a pandas DataFrame
df = pd.DataFrame(stock_data, columns=['Ticker Name', 'Price To Earning Ratio', 'Price To Book Ratio', 'PEG ratio'])

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="stock_database_1",
    user="erik",
    password=" "
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Define the SQL query to insert data into the stock_data table
update_query = """UPDATE stock_data SET"""

# Insert the data into the stock_data table one row at a time
for row in df.itertuples(index=False):
    full_query = update_query
    full_query += " price_to_earnings_ratio = %s, price_to_book_ratio = %s, peg_ratio = %s" % row[1:]
    full_query += " WHERE ticker_name = '%s'" % row[0]
    cur.execute(full_query, row)

# Commit the changes to the database and close the connection
conn.commit()
cur.close()
conn.close()

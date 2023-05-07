import yfinance as yf
import pandas as pd
import psycopg2

# Download the list of companies in the S&P500
sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = sp500.Symbol.tolist()
# Define the columns we want to retrieve for each stock
cols = ['shortName', 'marketCap', 'trailingPE', 'priceToBook', 'pegRatio']

# Download the stock data for all companies in the S&P500
stock_data = []
for ticker in tickers:
    try:
        info = yf.Ticker(ticker).info
        data = [ticker, info['shortName'], info['marketCap'], info['country'], 
                info['trailingPE'], info['priceToBook'], info['pegRatio']]
        stock_data.append(data)
    except:
        pass

# Convert the stock data to a pandas DataFrame
df = pd.DataFrame(stock_data, columns=['Ticker Name', 'Company Name', 'Market Cap', 'Region', 
                                        'Price To Earning Ratio', 'Price To Book Ratio', 'PEG ratio'])

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
insert_query = """
    INSERT INTO stock_data (ticker_name, company_name, market_cap, region, price_to_earnings_ratio, price_to_book_ratio, peg_ratio)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

# Insert the data into the stock_data table one row at a time
for row in df.itertuples(index=False):
    cur.execute(insert_query, row)

# Commit the changes to the database and close the connection
conn.commit()
cur.close()
conn.close()

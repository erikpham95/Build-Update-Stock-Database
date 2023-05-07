CREATE TABLE stock_data (
    ticker_name VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(255),
    market_cap NUMERIC(15,2),
    region VARCHAR(50),
    price_to_earnings_ratio NUMERIC(15,2),
    price_to_book_ratio NUMERIC(15,2),
    peg_ratio NUMERIC(15,2)
); 


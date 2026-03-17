import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'TSM', 'SMSN.IL', 'MSFT', 'NVDA', 'AMZN']

all_data = []

for ticker in tickers:

    df = yf.download(ticker, period="10d")
    df['Ticker'] = ticker
    df.reset_index(inplace=True)
    all_data.append(df)

final_data = pd.concat(all_data)
final_data.to_csv('stock_data.csv', index=False)

print("Stock data has been updated and saved to 'stock_data.csv'.")

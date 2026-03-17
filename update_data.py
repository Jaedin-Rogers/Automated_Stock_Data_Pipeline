import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'TSM', 'SMSN.IL', 'MSFT', 'NVDA', 'AMZN']

all_data = []

for ticker in tickers:

    df = yf.download(ticker, period="10d")
    df["Date"] = df.index
    df.reset_index(drop=True, inplace=True)
    

    df['Ticker'] = ticker
    all_data.append(df)

final_data = pd.concat(all_data, ignore_index=True)
final_data = final_data.sort_values(by=["Ticker", "Date"])

final_data.to_csv('stock_data.csv', index=False)

print("Stock data has been updated and saved to 'stock_data.csv'.")

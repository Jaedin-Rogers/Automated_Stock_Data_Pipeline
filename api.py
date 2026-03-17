import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Stock API! Use /stocks/{ticker} to get stock data."}

# Get all stocks data
@app.get("/stocks")
def get_stocks():
    
    df = pd.read_csv(
    "https://raw.githubusercontent.com/Jaedin-Rogers/Stock_Data_API/main/stock_data.csv"
)
    return df.to_dict(orient="records")

@app.get("/stocks/{ticker}")
def stock_head(ticker: str):
    df = pd.read_csv("stock_data.csv")
    filtered = df[df["Ticker"] == ticker]
    return filtered.head().to_dict(orient="records")

@app.get("/stocks/{ticker}/means")
def stock_means(ticker: str):
    df = pd.read_csv("stock_data.csv")
    filtered = df[df["Ticker"] == ticker]
    means = filtered.mean(numeric_only=True)
    return means.to_dict()


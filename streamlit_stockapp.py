import streamlit as st
from stock_functions import *
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price App")
st.write("Powered by FastAPI and Streamlit")

st.title("Stock Dashboard")

CSV_URL = "https://raw.githubusercontent.com/Jaedin-Rogers/Stock_Data_API/main/stock_data.csv"

@st.cache_data(ttl=600)
def load_data():
    return pd.read_csv(CSV_URL)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

def get_stock_data(ticker):
    return df[df["Ticker"] == ticker]

st.header("Apple vs TSM vs Samsung")

group1 = ["AAPL", "TSM", "SMSN.IL"]
for ticker in group1:
    st.subheader(ticker)
    stock = get_stock_data(ticker)
    st.dataframe(stock.head())

    means = stock.mean(numeric_only=True)
    st.write("Means:", means.to_dict())

fig1, ax1 = plt.subplots()

for ticker in group1:
    stock = get_stock_data(ticker)
    ax1.plot(pd.to_datetime(stock["Date"]), stock["Close"], label=ticker)

ax1.legend()
ax1.set_title("Closing Prices")

st.pyplot(fig1)



st.header("Microsoft vs Nvidia vs Amazon")

group2 = ["MSFT", "NVDA", "AMZN"]

for ticker in group2:
    st.subheader(ticker)

    stock = get_stock_data(ticker)
    st.dataframe(stock.head())

    means = stock.mean(numeric_only=True)
    st.write("Means:", means.to_dict())

fig2, ax2 = plt.subplots()

for ticker in group2:
    stock = get_stock_data(ticker)
    ax2.plot(pd.to_datetime(stock["Date"]), stock["Close"], label=ticker)

ax2.legend()
ax2.set_title("Closing Prices")

st.pyplot(fig2)

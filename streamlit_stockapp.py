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
    df = pd.read_csv(CSV_URL)
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
    st.subheader(f"{ticker} Means")
    cols = st.columns(len(means))
    
    for i, (metric, value) in enumerate(means.items()):
        if metric == "Volume":
            cols[i].metric(metric, f"{value:,.0f}")
        
        else:
            cols[i].metric(metric, f"{value:.2f}")

fig1, ax1 = plt.subplots()

for ticker in group1:
    stock = get_stock_data(ticker)
    ax1.plot(pd.to_datetime(stock["Date"]), stock["Close"], label=ticker)

ax1.legend()
ax1.set_title("Closing Prices")
fig1.autofmt_xdate()

st.pyplot(fig1)



st.header("Microsoft vs Nvidia vs Amazon")

group2 = ["MSFT", "NVDA", "AMZN"]

for ticker in group2:
    st.subheader(ticker)

    stock = get_stock_data(ticker)
    st.dataframe(stock.head())

    means = stock.mean(numeric_only=True)
    col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Open", f"{means['Open']:.2f}")

with col2:
    st.metric("High", f"{means['High']:.2f}")

with col3:
    st.metric("Low", f"{means['Low']:.2f}")

with col4:
    st.metric("Close", f"{means['Close']:.2f}")

with col5:
    st.metric("Volume", f"{means['Volume']:,.0f}")

fig2, ax2 = plt.subplots()

for ticker in group2:
    stock = get_stock_data(ticker)
    ax2.plot(pd.to_datetime(stock["Date"]), stock["Close"], label=ticker)

ax2.legend()
ax2.set_title("Closing Prices")
fig2.autofmt_xdate()

st.pyplot(fig2)

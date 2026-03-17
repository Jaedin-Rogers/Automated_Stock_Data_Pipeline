import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price App")
st.write("Powered by FastAPI and Streamlit")

st.title("Stock Dashboard")

API_URL = "http://127.0.1:8000"

# Fetch data from API
response = requests.get(f"{API_URL}/stocks")
df = pd.DataFrame(response.json())

st.header("Apple vs TSM vs Samsung")

group1 = ["AAPL", "TSM", "SMSN.IL"]

for ticker in group1:
    st.subheader(ticker)

    stock = df[df["Ticker"] == ticker]

    st.dataframe(stock.head())

    means = stock.mean(numeric_only=True)
    st.write("Means:", means.to_dict())

fig1, ax1 = plt.subplots()

for ticker in group1:
    stock = df[df["Ticker"] == ticker]
    ax1.plot(pd.to_datetime(stock["Date"]), stock["Close"], label=ticker)

ax1.legend()
ax1.set_title("Closing Prices")

st.pyplot(fig1)



st.header("Microsoft vs Nvidia vs Amazon")

group2 = ["MSFT", "NVDA", "AMZN"]

for ticker in group2:
    st.subheader(ticker)

    stock = df[df["Ticker"] == ticker]

    st.dataframe(stock.head())

    means = stock.mean(numeric_only=True)
    st.write("Means:", means.to_dict())

fig2, ax2 = plt.subplots()

for ticker in group2:
    stock = df[df["Ticker"] == ticker]
    ax2.plot(pd.to_datetime(stock["Date"]), stock["Close"], label=ticker)

ax2.legend()
ax2.set_title("Closing Prices")

st.pyplot(fig2)
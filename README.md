# 📈 Stock Data Dashboard

🔗 Live App: https://stockdataapi-jr.streamlit.app/  
📁 Repo: https://github.com/Jaedin-Rogers/Stock_Data_API

## 🚀 Overview
End-to-end data pipeline and dashboard that collects, processes, and visualizes stock data for companies like Apple, Microsoft, Nvidia, Amazon, TSM, and Samsung.

## ⚙️ Tech Stack
Python • pandas • matplotlib • yfinance • Streamlit *(FastAPI + GitHub Actions planned)*

## 📊 Features
- Time-series stock price charts  
- Cleaned, structured dataset  
- Summary metrics (Open, High, Low, Close, Volume)  
- Modular, API-ready code  
- Live deployed dashboard  

## ▶️ Run Locally
```bash
git clone https://github.com/Jaedin-Rogers/Stock_Data_API.git
cd Stock_Data_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py

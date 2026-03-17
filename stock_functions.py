
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# Create function that downloads stock data automatically and prints
def download_stock(ticker, period = "10d"):
    data = yf.download(ticker, period=period)
    return data

def show_head(data):
    return data.head().to_dict()

# Function used to compute means
def show_means(data):
    means = data.mean()
    means.index = [str(col) for col in means.index]
    return means.to_dict()

# Function used to set x(date) y(closing price)
def closed(data, ticker):
    x=data.index
    y=data[('Close', ticker)]
    return x, y


# Create function used to generate 3 plots for closing prices
def plot_three_stocks(x1, y1, x2, y2, x3, y3, title,
                     label1, label2, label3,
                     color1, color2, color3):

    fig, (ax1, ax2, ax3) = plt.subplots(3,1,sharex=True)

    fig.suptitle(title)

    ax1.plot(x1, y1, 'o-', color=color1)
    ax1.set_ylabel(label1)

    ax2.plot(x2, y2, 'o-', color=color2)
    ax2.set_ylabel(label2)

    ax3.plot(x3, y3, 'o-', color=color3)
    ax3.set_ylabel(label3)

    for ax in (ax1, ax2, ax3):
        ax.set_xlabel("Date")
        ax.tick_params(axis='x', rotation=90)

    plt.tight_layout()

    return fig

appl_data = download_stock('AAPL')
tsm_data = download_stock('TSM')
sam_data = download_stock('SMSN.IL')

show_head(appl_data)
show_head(tsm_data)
show_head(sam_data)

show_means(appl_data)
show_means(tsm_data)
show_means(sam_data)

x1, y1 = closed(appl_data, 'AAPL')
x2, y2 = closed(tsm_data, 'TSM')
x3, y3 = closed(sam_data, 'SMSN.IL')

plot_three_stocks(x1, y1, x2, y2, x3, y3, 'Apple Vs. TSM Vs. Samsung Stock Tracking',
                 'Apple Stock', 'TSM Stock', 'Samsung Stock',
                 'red', 'blue', 'gold'
                 )
plt.show()



micro_data = download_stock('MSFT')
nvda_data = download_stock('NVDA')
amzn_data = download_stock('AMZN')

show_head(micro_data)
show_head(nvda_data)
show_head(amzn_data)    

show_means(micro_data)
show_means(nvda_data)
show_means(amzn_data)

x1, y1 = closed(micro_data, 'MSFT')
x2, y2 = closed(nvda_data, 'NVDA')
x3, y3 = closed(amzn_data, 'AMZN')

plot_three_stocks(x1, y1, x2, y2, x3, y3, 'Microsoft Vs. Nvidia Vs. Amazon Stock Tracking',
                 'Microsoft Stock', 'Nvidia Stock', 'Amazon Stock',
                 'green', 'orange', 'purple'
                 )
plt.show()



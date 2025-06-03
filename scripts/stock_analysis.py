# stock_analysis.py

import pandas as pd
import talib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

class StockAnalyzer:
    def __init__(self, stock_name: str, filepath: str):
        self.stock_name = stock_name
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.filepath, parse_dates=["Date"])
        df.sort_values("Date", inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df

    def compute_indicators(self) -> pd.DataFrame:
        df = self.data.copy()

        # Ensure no NaN values in essential columns
        df = df.dropna(subset=["Close"])

        # Add TA-Lib indicators
        df["SMA_20"] = talib.SMA(df["Close"], timeperiod=20)
        df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)
        df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
        macd, macd_signal, _ = talib.MACD(df["Close"], fastperiod=12, slowperiod=26, signalperiod=9)
        df["MACD"] = macd
        df["MACD_Signal"] = macd_signal

        self.data = df
        return df

    def save_with_indicators(self, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.data.to_csv(output_path, index=False)

    def plot(self):
        df = self.data.copy()

        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                            vertical_spacing=0.1,
                            row_heights=[0.7, 0.3])

        # Candlestick
        fig.add_trace(
            go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name="Price"
            ), row=1, col=1)

        # SMA lines
        fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_20'], mode='lines', name='SMA 20', line=dict(color='blue')), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_50'], mode='lines', name='SMA 50', line=dict(color='red')), row=1, col=1)

        # Volume
        fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume'), row=2, col=1)

        fig.update_layout(title=f"{self.stock_name} Stock Price & Indicators",
                          xaxis_title="Date", yaxis_title="Price",
                          template="plotly_white", height=700)

        fig.show()

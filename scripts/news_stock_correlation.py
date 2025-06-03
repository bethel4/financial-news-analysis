import pandas as pd
from textblob import TextBlob
import os

# Define the SentimentCorrelationAnalyzer class
class SentimentCorrelationAnalyzer:
    def __init__(self, stock_df: pd.DataFrame, news_df: pd.DataFrame):
        self.stock_df = stock_df.copy()
        self.news_df = news_df.copy()

    def calculate_sentiment(self):
        self.news_df['date'] = pd.to_datetime(self.news_df['date'], format='ISO8601', errors='coerce')
        self.news_df['sentiment'] = self.news_df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        daily_sentiment = self.news_df.groupby(self.news_df['date'].dt.date)['sentiment'].mean()
        daily_sentiment.index = pd.to_datetime(daily_sentiment.index)
        return daily_sentiment

    def calculate_daily_returns(self):
        self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'])
        self.stock_df.set_index('Date', inplace=True)
        self.stock_df['Daily Return'] = self.stock_df['Close'].pct_change()
        return self.stock_df['Daily Return']

    def compute_correlation(self):
        sentiment_series = self.calculate_sentiment()
        return_series = self.calculate_daily_returns()
        aligned_df = pd.concat([sentiment_series, return_series], axis=1, join='inner')
        aligned_df.columns = ['Sentiment', 'Return']
        correlation = aligned_df.corr().iloc[0, 1]
        return correlation, aligned_df


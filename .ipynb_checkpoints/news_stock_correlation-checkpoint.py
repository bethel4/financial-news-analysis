# scripts/news_stock_correlation.py

import pandas as pd
from textblob import TextBlob

def calculate_sentiment(text: str) -> float:
    """Returns polarity score (-1 to 1) for a headline"""
    return TextBlob(text).sentiment.polarity

def preprocess_news(news_df: pd.DataFrame) -> pd.DataFrame:
    """Adds sentiment scores and formats the date column"""
    news_df = news_df.copy()
    news_df['date'] = pd.to_datetime(news_df['date'])
    news_df['sentiment'] = news_df['headline'].apply(calculate_sentiment)
    return news_df

def preprocess_stock(stock_df: pd.DataFrame) -> pd.DataFrame:
    """Prepares stock data by parsing dates and calculating returns"""
    stock_df = stock_df.copy()
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    stock_df = stock_df.sort_values('Date')
    stock_df['return'] = stock_df['Close'].pct_change()
    return stock_df

def merge_and_analyze(stock_df: pd.DataFrame, news_df: pd.DataFrame) -> pd.DataFrame:
    """Merges news and stock by date and calculates correlation"""
    # Group news by day and average sentiment
    daily_sentiment = news_df.groupby(news_df['date'].dt.date)['sentiment'].mean().reset_index()
    daily_sentiment.columns = ['Date', 'avg_sentiment']
    daily_sentiment['Date'] = pd.to_datetime(daily_sentiment['Date'])

    merged = pd.merge(stock_df, daily_sentiment, on='Date', how='inner')
    merged.dropna(subset=['return', 'avg_sentiment'], inplace=True)

    correlation = merged['avg_sentiment'].corr(merged['return'])
    return merged, correlation

import pandas as pd
from scripts.news_stock_correlation import SentimentCorrelationAnalyzer

# Define stock data paths and associated tickers
stock_files = {
    "META": "data/META_historical_data.csv",
    "TSLA": "data/TSLA_historical_data.csv",
    "MSFT": "data/MSFT_historical_data.csv",
    "AAPL": "data/AAPL_historical_data.csv",
    "AMZN": "data/AMZN_historical_data.csv",
    "NVDA": "data/NVDA_historical_data.csv",
    "GOOG": "data/GOOG_historical_data.csv",
}

# Load the main news file
news_df = pd.read_csv("..data/raw_analyst_ratings.csv.csv")
news_df['date'] = pd.to_datetime(news_df['date'], format='ISO8601').dt.date

# Loop through each ticker and analyze correlation
for ticker, filepath in stock_files.items():
    print(f"\nAnalyzing {ticker}...")

    stock_df = pd.read_csv(filepath)
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    stock_df = stock_df.sort_values("Date")

    news_ticker = news_df[news_df['stock'] == ticker]

    analyzer = SentimentCorrelationAnalyzer(ticker)
    result_df, correlation = analyzer.run_correlation_analysis(stock_df, news_ticker)

    print(f"Correlation between daily returns and sentiment for {ticker}: {correlation:.4f}")
    print(result_df[['Date', 'Close', 'Sentiment', 'Daily_Returns']].dropna().head())

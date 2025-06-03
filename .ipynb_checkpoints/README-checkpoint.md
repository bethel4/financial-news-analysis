
# Financial News Sentiment and Stock Correlation Analysis

This project analyzes the relationship between financial news sentiment and stock market movements. It focuses on how news headlines impact daily stock returns for companies like META, AAPL, TSLA, MSFT, and GOOGL.

## Project Structure
financial-news-analysis/
│
├── data/ # Contains stock CSV files and news dataset
│ ├── META_historical_data.csv
│ ├── TSLA_historical_data.csv
│ ├── ...
│ └── raw_analyst_ratings.csv # News headlines with stock labels
│
├── app/
│ └── main.py # Dashboard or app logic (future use)
│
├── run_news_correlation.py # Main script to run sentiment correlation analysis
├── sentiment_analysis.py # Contains SentimentCorrelationAnalyzer class
├── requirements.txt
└── README.md




## Features

- **Sentiment Analysis**: Assigns sentiment polarity scores to each headline using TextBlob.
- **Date Normalization**: Converts and aligns date formats between news and stock datasets using ISO 8601.
- **Stock Return Calculation**: Computes daily percentage change from closing prices.
- **Aggregation**: Averages daily sentiment scores if multiple headlines are published on the same day.
- **Correlation Analysis**: Computes Pearson correlation between sentiment scores and daily returns.
- **Visualization**: Plots:
  - Time series of sentiment vs. stock returns
  - Sentiment vs. return scatter plots

## How to Run

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
### Run the analysis
python run_news_correlation.py

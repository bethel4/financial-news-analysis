
import os
from scripts.stock_analysis import StockAnalyzer

# Define stock files
stock_files = {
    "META": "data/META_historical_data.csv",
    "TSLA": "data/GOOG_historical_data.csv",
    "MSFT": "data/MSFT_historical_data.csv",
    "AAPL": "data/AAPL_historical_data.csv",
    "AMZN": "data/AMZN_historical_data.csv",
    "NVDA": "data/NVDA_historical_data.csv",
    "GOOG": "data/GOOG_historical_data.csv",
}

# Run analysis for each
for stock, path in stock_files.items():
    print(f"\n Analyzing {stock} from {path}")
    analyzer = StockAnalyzer(stock_name=stock, filepath=path)
    analyzer.compute_indicators()
    analyzer.save_with_indicators(f"output/{stock}_with_indicators.csv")
    analyzer.plot()

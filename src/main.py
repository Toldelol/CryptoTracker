import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.logger import setup_logger
from utils.data_fetcher import CryptoFetcher
from utils.data_processor import process_data

try:
    import pandas as pd  # kräver att pandas är installerat
    use_pandas = True
except ImportError:
    use_pandas = False

logger = setup_logger()

def main():
    logger.info("Starting CryptoTracker - Fetching top 7 coins")

    fetcher = CryptoFetcher()
    data = fetcher.fetch_top_7_coins()
    if data:
        # Extrahera priser för processering
        prices = [coin['current_price'] for coin in data if 'current_price' in coin]
        avg, change = process_data(prices)
        
        # Visa data
        logger.info(f"Processed top 7 coins: Avg price {avg:.2f} USD, Overall change {change:.2f}%")
        print(f"Average price: {avg:.2f} USD")
        print(f"Overall price change: {change:.2f}%")
        
        if use_pandas:
            # Skapa DataFrame för snygg tabell
            df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap']]
            df.columns = ['Name', 'Symbol', 'Price (USD)', 'Market Cap (USD)']
            print("\nTop 7 Coins:\n")
            print(df.to_string(index=False))
        else:
            # Enkel print om ingen pandas
            print("\nTop 7 Coins:")
            for coin in data:
                print(f"{coin['name']} ({coin['symbol']}): Price ${coin['current_price']}, Market Cap ${coin['market_cap']}")
    else:
        logger.warning("No data fetched from API")
        sys.exit(1)

if __name__ == "__main__":
    main()
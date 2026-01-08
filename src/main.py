import sys
from utils.logger import setup_logger
from utils.data_fetcher import CryptoFetcher
from utils.data_processor import process_data

logger = setup_logger()

def main():
    logger.info("Starting CryptoTracker")
    
    # Säker input
    try:
        crypto = input("Enter crypto (e.g., bitcoin): ").strip().lower()
        if not crypto.isalpha():
            raise ValueError("Invalid input: Only letters allowed")
    except ValueError as e:
        logger.error(f"Input error: {e}")
        sys.exit(1)
    
    fetcher = CryptoFetcher()
    price = fetcher.fetch_price(crypto)
    if price:
        # Simulera lista av priser för bearbetning (i verkligheten, hämta fler)
        prices = [price, price * 1.05]  # Demo: Två priser
        avg, change = process_data(prices)
        print(f"Price: {price} USD")
        print(f"Avg: {avg}, Change: {change}%")
        logger.info(f"Processed {crypto}: Avg {avg}, Change {change}")
    else:
        logger.warning("No price data")

if __name__ == "__main__":
    main()
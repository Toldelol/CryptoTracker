from coingecko import CoinGeckoAPI

class CryptoFetcher:
    def __init__(self):
        self.api = CoinGeckoAPI()
    
    def fetch_price(self, crypto_id):
        try:
            data = self.api.get_price(ids=crypto_id, vs_currencies='usd')
            return data.get(crypto_id, {}).get('usd')
        except Exception as e:
            raise ValueError(f"Error fetching price: {e}")
import requests

class CryptoFetcher:
    def fetch_top_7_coins(self):
        url = 'https://api.coingecko.com/api/v3/coins/markets'
        params = {
            'vs_currency': 'usd',  # Valuta: USD
            'order': 'market_cap_desc',  # Sortera efter market cap fallande
            'per_page': 7,  # Hämta 7 coins
            'page': 1,  # Första sidan
            'sparkline': False  # Inga grafer behövs
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Kastar fel om inte 200 OK
            return response.json()  # Returnerar lista med dicts (coins)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from CoinGecko: {e}")
            return None
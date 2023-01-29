import random

def random_price():
  crypto_currencies = ['Bitcoin', 'Ethereum', 'Binance Coin', 'Cardano', 'Dogecoin']
  crypto_prices = {}
  for crypto in crypto_currencies:
    crypto_prices[crypto] = round(random.uniform(1, 100000), 2)
  return crypto_prices

print(random_price())
))

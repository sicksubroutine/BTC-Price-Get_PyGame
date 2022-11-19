import requests
price = 0
def btc_price_get():
  global price
  key = "https://api.kraken.com/0/public/Ticker?pair=xbtusd"
  r = requests.get(key)
  data = r.json()["result"]["XXBTZUSD"]["c"]
  price = round(float(data[0]))
  return price
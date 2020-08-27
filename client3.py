import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
  stock = quote['stock']
  bid_price = 117.00
  ask_price = 142.50
  price = (bid_price+ask_price/2)
  return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
  price_a = 142.50
  price_b = 117.00
  Ratio = price_a / price_b
  return Ratio

# Main
if __name__ == "__main__":

	# Query the price once every N seconds.
	
  for i in iter(range(500)):
    quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
    Ratio= getRatio(142.50, 117.00)
    print ("Ratio %s" % getRatio(142.50, 117.00))

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
    print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
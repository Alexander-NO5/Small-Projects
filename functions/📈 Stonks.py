# $AMC stock prices (in dollars) for 20 weekdays:
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
  a = a - 1
  return max(stock_prices[a:b])

def min_price(a, b):
  a = a - 1
  return min(stock_prices[a:b])

print(price_at(20))
print(max_price(1, 8))
print(min_price(10, 16))

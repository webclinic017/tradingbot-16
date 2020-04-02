import prices
import scraper

stocks = scraper.get_top_gainers()[0:5]
print(prices.get_latest_prices(stocks))
import requests

url = "https://www.binance.com/api/v3/uiKlines?limit=1000&symbol=BTCUSDT&interval=1d"

response = requests.request("GET", url)
print(response.json())
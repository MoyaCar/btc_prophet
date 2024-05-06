import requests
import time
from config import API_KEY

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/price"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl"}

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response = response.json()
response_time = response['data']['timestamp']
response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response_time))
response['data']['timestamp'] = response_time
print(response)

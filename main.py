import logging
import requests
import pandas as pd
from config import API_KEY
logging.basicConfig(level=logging.INFO)

def get_historic_price():
	url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
	querystring = {
		"referenceCurrencyUuid":"yhjMzLPhuIDl", #USD id
		"timePeriod":"30d"
		}

	headers = {
		"X-RapidAPI-Key": API_KEY,
		"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
	}
	try:
		response = requests.get(url, headers=headers, params=querystring)
	except requests.exceptions.RequestException as e:
		logging.error(e)
		exit()

	if response.status_code != 200:
		logging.error(f"API returned status code {response.status_code}")
		logging.info(f"Raw response: {response.json()}")
		exit()
	return response.json()


def convert_to_pandas(raw_data):
	df = pd.DataFrame(raw_data)
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
	df['price'] = pd.to_numeric(df['price'])
	return df

raw_data = get_historic_price()
df = convert_to_pandas(raw_data['data']['history'])
candled_price = df.groupby(pd.Grouper(key='timestamp', freq='1D')).agg(['first', 'max', 'min', 'last'])
candled_price = candled_price['price']


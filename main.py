import logging
import pandas as pd
import time
import json

logging.basicConfig(level=logging.INFO)

with open('./historical_data/daily_price_new.json', 'r') as f:
	newly_data = json.load(f)
	f.close()

newly_data =newly_data['data']['klines']

data_for_pandas = [
	{
		'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(datapoint[0])/1000)),
  		'open': float(datapoint[1]),
		'close': float(datapoint[2]),
		'high': float(datapoint[3]),
		'low': float(datapoint[4]),
		'volume': float(datapoint[5]),
	} for datapoint in newly_data
]
df = pd.DataFrame(data_for_pandas)

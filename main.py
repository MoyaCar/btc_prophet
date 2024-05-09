import logging
import pandas as pd
import time
import json

logging.basicConfig(level=logging.INFO)

with open('./historical_data/daily_price_new.json', 'r') as f:
	newly_data = json.load(f)
	f.close()

with open('./historical_data/daily_price.json', 'r') as f:
	old_data = json.load(f)
	f.close()

price_data = old_data['data']['klines'] + newly_data['data']['klines']
data_for_pandas = [
	{
		'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(datapoint[0])/1000)),
  		'open': float(datapoint[1]),
		'close': float(datapoint[2]),
		'high': float(datapoint[3]),
		'low': float(datapoint[4]),
		'volume': float(datapoint[5]),
	} for datapoint in price_data
]
df = pd.DataFrame(data_for_pandas).sort_values('timestamp').set_index('timestamp')


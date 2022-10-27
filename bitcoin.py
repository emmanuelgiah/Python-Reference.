import requests
import time
from datetime import datetime

bitcoin_price_threshold = 10000
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/bitcoin_price_update/with/key/42H_2gI6w6-TuZ3zXFfRV'

def get_latest_bitcoin_price():
	response = requests.get(bitcoin_api_url)
	response_json = response.json()
	#convert the price to a floating point number
	return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
	#the payload that will be sent to ifttt service
	data = {'value1': value}
	#inserts our desired event
	ifttt_event_url = ifttt_webhook_url.format(event)
	#sends a http post request to the webhook url
	requests.post(ifttt_event_url, json=data)

def main():
	bitcoin_history = []
	while True:
		price = get_latest_bitcoin_price();
		date = datetime.now()
		bitcoin_history.append({"date": date, "price":price})

		#send an emergency notification 
		if price < bitcoin_price_threshold:
			post_ifttt_webhook("bitcoin_price_emergency", price)

		#send a telegram notification
		#once we have 5 items in our bitcoin_history send an update
		if len(bitcoin_history) == 5:
			post_ifttt_webhook("bitcoin_price_update",
				format_bitcoin_history(bitcoin_history))

			#Reset the history
			bitcoin_history = [];

		#Sleep for 5 minutes
		#(for testing purpose you can set it to a lower number)
		time.sleep(1);

def format_bitcoin_history(bitcoin_history):
	rows = []
	for bitcoin_price in bitcoin_history:
		#formats the date into a string: '24.02.2018 15:09'
		date = bitcoin_price['date'].strftime("$d.%m.%Y %H:%M")
		price = bitcoin_price['price']
		#<b> (bold) tag creates bolded text
		rows = '{}: $<b>{}</b>'.format(date, price)
		rows.append(row)
	return '<br>'.join(rows)

if __name__ == "__main__":
	main();





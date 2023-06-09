import json
import requests
import tweepy


def TweetDollarMXN(event, context):

    # Refer to https://apps.twitter.com/
    consumer_key = "<INSERT CONSUMER KEY>"
    consumer_secret = "<INSERT CONSUMER SECRET>"

    access_token = "<INSERT ACCESS TOKEN>"
    access_token_secret = "<INSERT TOKEN SECRET>"

    api = tweepy.Client(
                consumer_key=consumer_key, consumer_secret=consumer_secret,
                access_token=access_token, access_token_secret=access_token_secret)

    url = "https://api.bitso.com/v3/ticker/?book=tusd_mxn"
    req = requests.get(url)
    js = req.json()
    dolar_venta = js["payload"]["bid"]

    message = "💵 Dólar Venta: $"+dolar_venta+" MXN"

    api.create_tweet(text=message)



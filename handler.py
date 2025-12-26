import json
import os
import requests
import tweepy
from dotenv import load_dotenv

def get_bitso_bid(book):
    url = f"https://api.bitso.com/v3/ticker/?book={book}"
    req = requests.get(url)
    js = req.json()
    return float(js["payload"]["bid"])


def TweetDollarMXN(event, context):
    # Load environment variables
    load_dotenv()

    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SEC = os.getenv("CONSUMER_SEC")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_SECRE = os.getenv("ACCESS_SECRE")

    if not CONSUMER_KEY or not ACCESS_TOKEN:
        print("Error: Please add Twitter tokens in .env file.")
        exit(1)

    # Refer to https://apps.twitter.com/
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SEC

    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRE

    api = tweepy.Client(
                consumer_key=consumer_key, consumer_secret=consumer_secret,
                access_token=access_token, access_token_secret=access_token_secret)

    dolar_venta = get_bitso_bid("usd_mxn")
    eth_venta = get_bitso_bid("eth_mxn")
    btc_venta = get_bitso_bid("btc_mxn")

    message = f"💵 Dólar Venta: ${dolar_venta:.2f} MXN\nEthereum Venta: ${eth_venta:.2f} MXN\nBitcoin Venta: ${btc_venta:.2f} MXN"

    api.create_tweet(text=message)



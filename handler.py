import json
import requests
import tweepy
from dotenv import load_dotenv


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

    url = "https://api.bitso.com/v3/ticker/?book=tusd_mxn"
    req = requests.get(url)
    js = req.json()
    dolar_venta = float(js["payload"]["bid"])

    message = f"💵 Dólar Venta: ${dolar_venta:.2f} MXN"

    api.create_tweet(text=message)



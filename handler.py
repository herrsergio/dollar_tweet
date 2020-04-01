import json
import requests
import tweepy


def TweetDollarMXN(event, context):

    # Refer to https://apps.twitter.com/
    consumer_key = "<INSERT CONSUMER KEY>"
    consumer_secret = "<INSERT CONSUMER SECRET>"

    access_token = "<INSERT ACCESS TOKEN>"
    access_token_secret = "<INSERT TOKEN SECRET>"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    url = "https://api.bitso.com/v3/ticker/?book=tusd_mxn"
    req = requests.get(url)
    js = req.json()
    dolar_venta = js["payload"]["bid"]

    message = "Dólar Venta "+dolar_venta

    api.update_status(status=message)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


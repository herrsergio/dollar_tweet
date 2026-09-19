import json
import os
import requests
import grapheme
from atproto import Client
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

MAX_GRAPHEMES = 300  # Bluesky post limit

def get_usd_history():
    try:
        # AWS Lambda runs in UTC; use UTC-6 for Mexico Time to keep dates consistent
        end_date = datetime.now(timezone.utc) - timedelta(hours=6)
        start_date = end_date - timedelta(days=7)
        url = f'https://api.frankfurter.dev/v1/{start_date.strftime("%Y-%m-%d")}..{end_date.strftime("%Y-%m-%d")}?base=USD&symbols=MXN'
        req = requests.get(url).json()
        rates = req.get('rates', {})
        if not rates:
            return 0.0, 0.0
        dates = sorted(list(rates.keys()))
        price_7d = rates[dates[0]]['MXN']
        price_now = rates[dates[-1]]['MXN']
        change_pct = (price_now - price_7d) / price_7d * 100
        return price_now, change_pct
    except Exception as e:
        print(f"Error fetching USD history: {e}")
        return 0.0, 0.0


def get_coingecko_history(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=mxn&days=7"
    response = requests.get(url)
    data = response.json()
    prices = data["prices"]

    price_now = prices[-1][1]
    price_7d = prices[0][1]

    change_pct = (price_now - price_7d) / price_7d * 100

    return price_now, change_pct


def TweetDollarMXN(event, context):
    # Load environment variables
    load_dotenv()

    BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
    BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

    if not BLUESKY_HANDLE or not BLUESKY_APP_PASSWORD:
        print("Error: Please add BLUESKY_HANDLE and BLUESKY_APP_PASSWORD in .env file.")
        exit(1)

    # App password is created in Bluesky Settings -> App Passwords
    client = Client()
    client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

    dolar_p, dolar_c = get_usd_history()
    eth_p, eth_c = get_coingecko_history("ethereum")
    btc_p, btc_c = get_coingecko_history("bitcoin")

    def format_line(name, price, change):
        emoji = "🔼" if change >= 0 else "🔽"
        sign = "+" if change > 0 else ""
        return f"{name:<11} ${price:>12,.2f} MXN {emoji} {sign}{change:.1f}% (7d)"

    message = (
        f"💵\n"
        f"{format_line('Dollar:', dolar_p, dolar_c)}\n"
        f"{format_line('Ethereum:', eth_p, eth_c)}\n"
        f"{format_line('Bitcoin:', btc_p, btc_c)}"
    )

    # Bluesky counts length in graphemes, not code points; truncate if needed.
    if grapheme.length(message) > MAX_GRAPHEMES:
        message = grapheme.slice(message, 0, MAX_GRAPHEMES - 1) + "…"

    client.send_post(text=message)



import requests
import time
from telegram import Bot, ParseMode

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # استبدل بالتوكن الخاص بك
CHANNEL_ID = '@your_channel_username'  # استبدل بمعرف القناة

bot = Bot(token=TOKEN)

coins = {
    'bitcoin': '🟠',
    'ethereum': '🟣',
    'binancecoin': '🟡',
    'ripple': '💧',
    'solana': '☀️',
    'toncoin': '🔵',
    'cardano': '🔷',
    'dogecoin': '🐕',
    'polkadot': '⚫',
    'litecoin': '⚡',
    'chainlink': '🔗',
    'stellar': '🌟',
    'vechain': '🛡️',
    'tron': '🚀',
    'monero': '🧡',
    'eos': '🅴',
    'tezos': '✝️',
    'cosmos': '☄️',
    'theta-token': '🎬',
    'filecoin': '📁',
    'uniswap': '🦄',
    'aave': '🏦',
    'shiba-inu': '🐕',
    'algorand': '🔵',
    'avalanche-2': '🏔️',
    'crypto-com-chain': '💳',
    'elrond-erd-2': '🌐',
    'decentraland': '🌍',
    'the-graph': '📊',
    'maker': '⚙️',
    'compound-governance-token': '🏛️',
    'bitcoin-cash': '💵',
    'dash': '🚗',
    'zcash': '🛡️',
    'waves': '🌊',
    'neo': '🟢',
    'iota': '🔺',
    'ftx-token': '🦊',
    'celsius-degree-token': '🌡️',
    'basic-attention-token': '🎭',
    'enjincoin': '🎮',
    'chiliz': '🏟️',
    'huobi-token': '🔥',
    'kusama': '🦋',
    'pancakeswap-token': '🥞',
    'hedera-hashgraph': '🌿',
    'bitTorrent': '🎵',
    'loopring': '🔄',
    'yearn-finance': '📈',
    'sushi': '🍣',
    'zilliqa': '⚡',
}

def get_prices():
    ids = ','.join(coins.keys())
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd'
    response = requests.get(url)
    return response.json()

def format_message(prices):
    lines = ["*Top 50 Crypto Prices Update:*", ""]
    for coin, emoji in coins.items():
        price = prices.get(coin, {}).get('usd')
        if price is not None:
            price_str = f"${price:,.4f}" if price < 1

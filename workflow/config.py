import os

from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv('HOST', None)

TG_AP = os.getenv('TG_AP', None)

HEADERS = {"accept": "application/json"}

URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2CEthereum%2CBinanceCoin%2CCardano&vs_currencies=usd'

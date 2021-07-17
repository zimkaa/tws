import os

from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv('HOST', None)

TG_AP = os.getenv('TG_AP', None)

HEADERS = {"accept": "application/json"}

url_part_1 = "https://api.coingecko.com/api/v3/simple/price?"

url_part_2 = "ids=bitcoin%2CEthereum%2CBinanceCoin%2CCardano&vs_currencies=usd"

URL_GECKO = url_part_1 + url_part_2

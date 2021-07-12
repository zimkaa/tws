import os

from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv('TG_AP', None)

TG_AP = os.getenv('TG_AP', None)

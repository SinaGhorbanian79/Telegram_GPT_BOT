import requests
from dotenv import load_dotenv
import os
import telegram.ext

load_dotenv("api_key.env")

api_key = os.getenv("TELEGRAM_API_KEY")


print(dir(telegram.ext))

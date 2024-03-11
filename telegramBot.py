from dotenv import load_dotenv
import os
import telegram.ext
import asyncio


load_dotenv("api_key.env")

api_key = os.getenv("TELEGRAM_API_KEY")


print(api_key)

from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import asyncio


load_dotenv("api_key.env")

api_key = os.getenv("TELEGRAM_API_KEY")
bot_username = "@sinaGpt_bot"


# Commands
async def start_command(update: Update, Contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am Sina's Humble Assistant")


async def help_command(update: Update, Contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Please Contact My Master (Sina Ghorbanian) For any FFurther Assistant"
    )


# responses
def handle_responses(text: str) -> str:
    processed: str = text.lower()


# message
def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

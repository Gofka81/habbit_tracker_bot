from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import utils.token_setup as tstp
import json

TOKEN = tstp.get_api_token()  # Put your bot token in .env

WEBAPP_URL = "https://yourserver.com"  # Or http://localhost:8080 when testing

# Command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with a WebApp button."""
    keyboard = [
        [KeyboardButton(text="Open Habit Tracker", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Tap to open the Habit Tracker Web App:", reply_markup=reply_markup)

# Handle WebApp data
async def webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the data sent from the WebApp."""
    data = json.loads(update.message.web_app_data.data)
    habit = data.get("habit")
    status = data.get("status")
    await update.message.reply_text(f"Received habit: {habit}, status: {status}")

def main():
    """Start the bot."""
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_data))
    app.run_polling()

if __name__ == "__main__":
    main()

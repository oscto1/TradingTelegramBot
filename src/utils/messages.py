from telegram import Update
from telegram.ext import ContextTypes

async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, reply_markup=None):
    # If command/message
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    
    # If button
    elif update.callback_query:
        query = update.callback_query
        await query.message.reply_text(text, reply_markup=reply_markup)
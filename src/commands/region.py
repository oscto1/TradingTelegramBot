from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ContextTypes, ConversationHandler
from utils import REGIONS

MENU = 0

async def region(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [InlineKeyboardButton("North America", callback_data="na")],
        [InlineKeyboardButton("South America", callback_data="sa")],
        [InlineKeyboardButton("Europe", callback_data="eu")],
        [InlineKeyboardButton("Asia", callback_data="as")],
        [InlineKeyboardButton("Africa", callback_data="af")],
        [InlineKeyboardButton("Oceania", callback_data="oc")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Select your region: ", reply_markup=reply_markup
    )
    return MENU

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    user_id = update.effective_user.id

    region = REGIONS.get(query.data)
    await query.edit_message_text(text=f"You selected {region}")
    return ConversationHandler.END

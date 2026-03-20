from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from utils import constants, messages
from database.users import get_user, set_region, ensure_user

async def region(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    reply_markup = None
    if(user and user["region"]):
        text = "You already selected a region."
    else:
        keyboard = [
            [InlineKeyboardButton("North America", callback_data="region_na")],
            [InlineKeyboardButton("South America", callback_data="region_sa")],
            [InlineKeyboardButton("Europe", callback_data="region_eu")],
            [InlineKeyboardButton("Asia", callback_data="region_as")],
            [InlineKeyboardButton("Africa", callback_data="region_af")],
            [InlineKeyboardButton("Oceania", callback_data="region_oc")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "Select your region:"

    await messages.send_message(update, context, text, reply_markup)
    # if(reply_markup != None):
    #     if(update.message):
    #         await update.message.reply_text(text, reply_markup=reply_markup)
    #     else:
    #         await update.callback_query.message.reply_text(text, reply_markup=reply_markup)
    # else:
    #     await update.message.reply_text(text)
        

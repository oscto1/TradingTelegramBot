from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from database.users import get_user, ensure_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    # await update.message.reply_text(f"Hello {user.first_name}! Welcome to the Creature Bot.")

    user_id = user.id
    ensure_user(user_id)
    db_user = get_user(user_id)
    if(not db_user["region"]):
        keyboard = [
            [InlineKeyboardButton("🌍 Select Region", callback_data="start_play")]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("🎁 Claim Daily", callback_data="daily")],
            [InlineKeyboardButton("🧬 Creatures", callback_data="creatures")],
            [InlineKeyboardButton("🌍 Change Region", callback_data="region_menu")],
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(f"Hello {user.first_name}!", reply_markup=reply_markup)
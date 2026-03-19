from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler
from database.users import create_user, get_user

STATE = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}! Welcome to the Creature Bot.")

    keyboard = [[InlineKeyboardButton("Play!", callback_data="start_game")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Start playing!", reply_markup=reply_markup)
    return STATE

async def startButton(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    userexist = get_user(user_id) != None
    print("user "+ str(user_id) + " exists: " + str(userexist))
    if(not userexist):
        create_user(user_id)
        await query.edit_message_text(text=f"Your user was created!")
    else:
        await query.edit_message_text(text=f"Some message!")    
    return ConversationHandler.END
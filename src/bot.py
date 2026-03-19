import logging
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ConversationHandler, MessageHandler, filters
from config import BOT_TOKEN
from commands.start import start, STATE, startButton
from commands.region import MENU, region, button
from database.db import init_db

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            STATE:[CallbackQueryHandler(startButton)],
        },
        fallbacks=[CommandHandler("start", start)]
    ))
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("region", region)],
        states={
            MENU:[CallbackQueryHandler(button)],
        },
        fallbacks=[CommandHandler("start", start)],
    ))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()

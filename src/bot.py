import logging
from telegram.ext import Application, CallbackQueryHandler, CommandHandler
from config import BOT_TOKEN
from commands.start import start
from commands.region import region
from commands.daily import daily
from database.db import init_db
from handlers.buttons import handle_buttons

# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# logger = logging.getLogger(__name__)

def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()
    
    # commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("region", region))
    app.add_handler(CommandHandler("daily", daily))

    # buttons
    app.add_handler(CallbackQueryHandler(handle_buttons))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()

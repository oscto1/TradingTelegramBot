from telegram import Update
from telegram.ext import ContextTypes
from database.users import ensure_user, get_user, set_region
from utils import REGIONS
from commands.region import region

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    ensure_user(user_id)
    data = query.data

    # START BUTTON
    if(data == "start_play"):
        await query.message.delete()  # optional (clean UI)
        await region(update, context)
        return
    
    # REGION SELECTION
    if data.startswith("region_"):
        region_code = data.split("_")[1]

        print(region_code)
        if region_code not in REGIONS:
            await query.edit_message_text("Invalid region.")
            return

        user = get_user(user_id)

        if user["region"]:
            await query.edit_message_text("You already selected a region.")
            return

        set_region(user_id, region_code)

        await query.edit_message_text(
            f"Your region is now {REGIONS[region_code]}"
        )
        return
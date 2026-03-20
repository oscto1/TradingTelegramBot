from telegram import Update
from telegram.ext import ContextTypes
from database.users import ensure_user, get_user, set_last_daily
from datetime import datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo
from utils import messages, mytime

RESET_HOUR = 2
TIMEZONE = "UTC"

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ensure_user(user_id)
    user = get_user(user_id)

    if can_claim_daily(user):
        now = datetime.now(timezone.utc)
        await messages.send_message(update, context, "Daily reward placeholder 🎁")
        set_last_daily(user_id, datetime.timestamp(now))
        # await update.message.reply_text("Daily reward placeholder 🎁")
    else:
        remaining = time_until_next_daily(user)
        await messages.send_message(update, context, f"Today's reward was already claimed! Try again in {mytime.td_hours(remaining)}h {mytime.td_minutes(remaining)}m")
        # await update.message.reply_text(f"Today's reward was already claimed! Wait {remaining}")


def can_claim_daily(user) -> bool:
    if user["last_daily"] is None:
        return True
    
    now = datetime.now(timezone.utc)
    tz = ZoneInfo(TIMEZONE)

    last_reset = get_last_reset(now, tz)

    last_utc_timestamp = datetime.fromtimestamp(
        user["last_daily"], tz=timezone.utc
    )
    return last_utc_timestamp < last_reset





def get_last_reset(now: datetime, tz: ZoneInfo) -> datetime:
    now_tz = now.astimezone(tz)

    today_reset = datetime.combine(now_tz.date(), time(hour=RESET_HOUR), tzinfo=tz)

    if(now_tz >= today_reset):
        return today_reset
    else:
        #before today's reset, use yesterday
        return today_reset - timedelta(days=1)
    



    
def time_until_next_daily(user) -> timedelta:
    if user["last_daily"] is None:
        return timedelta(0)

    now = datetime.now(timezone.utc)
    tz = ZoneInfo(TIMEZONE)

    last_reset = get_last_reset(now, tz)
    next_reset = last_reset + timedelta(days=1)

    last_utc_timestamp = datetime.fromtimestamp(
        user["last_daily"], tz=timezone.utc
    )

    if last_utc_timestamp >= last_reset:
        return next_reset - now
    
    return timedelta(0)
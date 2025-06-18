import os
import sys
import logging
from decouple import config
# ✅ Add the project root (D:\myproject) to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from asgiref.sync import sync_to_async

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# ✅ Now it's safe to import from your Django app
from api.models import TelegramUser

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



logging.basicConfig(level=logging.INFO)

from asgiref.sync import sync_to_async

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_user = update.effective_user

    await sync_to_async(TelegramUser.objects.get_or_create)(
        telegram_id=tg_user.id,
        defaults={
            "username": tg_user.username,
            "first_name": tg_user.first_name,
        }
    )

    await update.message.reply_text(f"Hey {tg_user.first_name}! You're now registered 🎉")

def main():
    TOKEN = config("TELEGRAM_BOT_TOKEN")  # Add this to .env
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()

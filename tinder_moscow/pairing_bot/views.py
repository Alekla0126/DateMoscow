from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater
from pairing_bot.models import UserProfile

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    
    # Check if user exists in the database or create a new one
    user_profile, created = UserProfile.objects.get_or_create(telegram_id=chat_id)
    if created:
        # Ask for gender and other introductory info
        context.bot.send_message(chat_id=chat_id, text=f"Hello {user.first_name}, please choose your gender.")
    else:
        context.bot.send_message(chat_id=chat_id, text=f"Welcome back {user.first_name}!")

def main() -> None:
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

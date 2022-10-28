import os
from telegram.ext import Filters, MessageHandler, Updater
from dotenv import load_dotenv
from googletrans import Translator

load_dotenv()
token = os.getenv('TOKEN')

updater = Updater(token=token)
translator = Translator()

def translate(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=translator.translate(update.message.text, dest='tr').text
    )

updater.dispatcher.add_handler(MessageHandler(Filters.text, translate))
updater.start_polling()
updater.idle()
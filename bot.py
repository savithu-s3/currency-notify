import telegram
from telegram.ext import Updater, CommandHandler

@app.route('/healthcheck')
def healthcheck():
    return "OK", 200

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot!")

updater = Updater(token='5938743745:AAH_vYTPnMWsol1fbtM_Ae5QOAe9Em-_qBw', use_context=True)
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()
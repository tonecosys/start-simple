from flask import Flask, request
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok', 200

def start(update, context):
    update.message.reply_text('Hello! This is your bot.')

def echo(update, context):
    update.message.reply_text(update.message.text)

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  

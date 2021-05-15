#!/usr/bin/python
import telegram
from telegram.ext import Updater, Dispatcher, CommandHandler
from red_alert import Alert
import logging
from snake import snake
import threading
import schedule

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = open('bot_token', 'r').read()

# setup the bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def red_alert():
    alert_obj = Alert()
    alerts = alert_obj.

def bot_ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Bot is up and running')

def send_snake(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=snake())

def run_bot


def main():
    # dispatcher.add_handler('start', )
    snake_handler = CommandHandler('snake', send_snake)
    dispatcher.add_handler(snake_handler)
    # t1 = threading.Thread (target=)
    updater.start_polling()


if __name__ == '__main__':
    main()

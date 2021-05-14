#!/usr/bin/python
import telegram
from telegram.ext import Updater, Dispatcher
from red_alert import Alert
import logging
from snake import snake

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = open('bot_token', 'r').read()

def red_alert():
    alert_obj = Alert()
    alert_obj.run()

def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler('start', )
    dispatcher.add_handler('snake', snake)
    test_bot = telegram.Bot(token=TOKEN)
    test_bot.

if __name__ == '__main__':
    main()
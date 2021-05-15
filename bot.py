#!/usr/bin/python
from telegram.ext import Updater, CommandHandler
from red_alert import Alert
import logging
from snake import snake
import threading
from time import sleep

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = open('bot_token', 'r').read()


class AuroraBot(object):
    def __init__(self, token, red_alert_places_filter=None):
        self.red_alert_places_filter = red_alert_places_filter
        self.run_red_alert = False
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    @staticmethod
    def _bot_ping(update, context):
        context.bot.send_message(chat_id=update.effective_message.chat_id, text='Bot is up and running')

    @staticmethod
    def _send_snake(update, context):
        context.bot.send_message(chat_id=update.effective_message.chat_id, text=snake())

    def _start_red_alert(self, update, context):
        if self.run_red_alert:
            context.bot.send_message(chat_id=update.effective_message.chat_id, text='Red alerts are already running...')
            return
        context.bot.send_message(chat_id=update.effective_message.chat_id, text='Red alert updates have been started')
        self.run_red_alert = True
        self.red_alert_thread = threading.Thread(target=self._run_red_alert, args=(update, context))
        self.red_alert_thread.start()

    def _stop_red_alert(self, update, context):
        if self.run_red_alert == False:
            context.bot.send_message(chat_id=update.effective_message.chat_id, text='Red alerts are already stopped...')
            return
        self.run_red_alert = False
        context.bot.send_message(chat_id=update.effective_message.chat_id, text='Red alert updates have been stopped')

    def _run_red_alert(self, update, context):
        alerts = Alert()
        while self.run_red_alert:
            new_alerts = alerts.check_for_update()
            if new_alerts:
                if self.red_alert_places_filter:
                    new_alerts = filter(lambda x: any(substr in x for substr in self.red_alert_places_filter),
                                        new_alerts)
                for new_alert in new_alerts:
                    context.bot.send_message(chat_id=update.effective_message.chat_id,
                                             text=alerts.notify(new_alert))
            sleep(2)

    def run(self):
        snake_handler = CommandHandler('snake', self._send_snake)
        red_alert_start_handler = CommandHandler('start', self._start_red_alert)
        red_alert_stop_handler = CommandHandler('stop', self._stop_red_alert)
        ping_handler = CommandHandler('ping', self._bot_ping)
        self.dispatcher.add_handler(snake_handler)
        self.dispatcher.add_handler(red_alert_start_handler)
        self.dispatcher.add_handler(red_alert_stop_handler)
        self.dispatcher.add_handler(ping_handler)
        self.updater.start_polling()


def main():
    test_bot = AuroraBot(TOKEN)
    test_bot.run()


if __name__ == '__main__':
    main()

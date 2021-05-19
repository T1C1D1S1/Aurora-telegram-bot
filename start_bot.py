#!/usr/bin/python
import bot

BOT_TOKEN = open('bot_token', 'r').read()
YESHUVIM_FILTER = ['בת חפר', 'רמת השרון', 'מודיעין', 'תל אביב', 'מתן', 'בנימינה', 'חיפה']

if __name__ == '__main__':
    bot_instance = bot.AuroraBot(BOT_TOKEN, YESHUVIM_FILTER)
    bot_instance.run()
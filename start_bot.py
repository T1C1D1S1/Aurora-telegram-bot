#!/usr/bin/python
import bot
import json


if __name__ == '__main__':
    # TODO: change token to be read from typer argument
    # TODO: change cities whitelist to be read from the alerts handler
    bot_token = open('bot_token.txt', 'r').read()
    red_alert_cities_whitelist = json.load(open('./modules/red_alert/cities_whitelist.json', 'r'))
    bot_instance = bot.AuroraBot(bot_token, red_alert_cities_whitelist)
    bot_instance.run()

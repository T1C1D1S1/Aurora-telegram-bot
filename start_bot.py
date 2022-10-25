#!/usr/bin/python
import json
import logging
import os.path

import typer

import _bot_backend

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main(token: str = typer.Argument("", help="Telegram bot token from BotFather to use"), red_alert: bool = False, inspirobot: bool = False, snake: bool = False):
    # TODO: change cities whitelist to be read from the alerts handler
    logger = logging.getLogger(__name__)

    if not token:
        print("No bot token has been supplied! trying to load from bot_token.txt")
        if os.path.exists("bot_token"):
            token = open("bot_token.txt", 'r').read()
        else:
            print("File bot_token.txt does not exist and no token had been supplied in arguments! quitting.")
            exit(-1)

    if not any([red_alert, inspirobot, snake]):
        print("No modules have been loaded! make sure you choose at least one")
        exit(-1)
    red_alert_cities_whitelist = json.load(open('./modules/red_alert/cities_whitelist.json', 'r'))
    logger.info("Starting bot")
    bot_instance = _bot_backend.AuroraBot(token, inspirobot, red_alert, snake, red_alert_cities_whitelist)
    bot_instance.run()


if __name__ == '__main__':
    typer.run(main)

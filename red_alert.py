#!/usr/bin/python
from hashlib import md5
from time import time, sleep
from typing import List

import requests

HASH_PART_1 = b"@Kobi*Snir-"
HASH_PART_2 = b"-#iOSLinks!"
SERVER = 'http://80.179.114.130/api2/stt.php'  # gets latest feed


class Alert(object):
    def __init__(self):
        # self.feed = self._extract_ids(self._get_feed())
        self.feed = self._get_feed()
        self.ids = self._get_ids()

    def run_loop(self):
        print('Alerts service is running...')
        while True:
            updates = self.check_for_update()
            if updates:
                for update in updates:
                    updates.remove(update)
                    print(self.notify(update))
            sleep(3)

    def check_for_update(self) -> list[dict]:
        new_feed = self._get_feed()
        updates_to_push = list(filter(lambda x: x['id'] not in self.ids, new_feed))
        if updates_to_push:
            self.ids = self._get_ids()
            return updates_to_push

    @staticmethod
    def notify(alert: dict) -> str:
        """
        Formats out an alert
        :param alert: An alert dict
        :return: The alert as a string
        """
        return f'{alert["date"]}\n{alert["message"]}'

    def _get_ids(self) -> List[str]:
        return list(map(lambda x: x['id'], self.feed))

    @staticmethod
    def _get_feed() -> List[dict]:
        """
        gets the current red alert feed from the alerts server
        :return: The list
        """
        timestamp = int(time() * 10000)
        request_hash = md5(HASH_PART_1 + str(timestamp).encode() + HASH_PART_2).hexdigest()
        result = requests.post(SERVER, data={'method': 'getFeed', 'ts': timestamp, 'hash': request_hash})
        return result.json()['feed']


def main():
    alerts = Alert()
    alerts.run_loop()


if __name__ == '__main__':
    main()

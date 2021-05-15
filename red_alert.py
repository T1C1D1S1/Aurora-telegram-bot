#!/usr/bin/python
from hashlib import md5
from time import time, sleep
import requests

HASH_PART_1 = b"@Kobi*Snir-"
HASH_PART_2 = b"-#iOSLinks!"
SERVER = 'http://80.179.114.130/api2/stt.php'  # gets latest feed


class Alert():
    def __init__(self):
        # self.feed = self._extract_ids(self._get_feed())
        self.feed = self._get_feed()
        self.ids = self._get_ids()

    def run_loop(self):
        print('Alerts is running...')
        while True:
            updates = self._check_for_update()
            if updates:
                for update in updates:
                    updates.remove(update)
                    self._notify(update)
            sleep(3)

    def _get_ids(self):
        return list(map(lambda x: x['id'], self.feed))

    def _check_for_update(self):
        new_feed = self._get_feed()
        updates_to_push = list(filter(lambda x: x['id'] not in self.ids, new_feed))
        if updates_to_push:
            self.ids = self._get_ids()
            return updates_to_push

    @staticmethod
    def _notify(alert):
        print(f'new red alert at {alert["message"]} at time {alert["date"]}')

    @staticmethod
    def _get_feed():
        timestamp = int(time() * 10000)
        request_hash = md5(HASH_PART_1 + str(timestamp).encode() + HASH_PART_2).hexdigest()
        result = requests.post(SERVER, data={'method': 'getFeed', 'ts': timestamp, 'hash': request_hash})
        return result.json()['feed']


def main():
    alerts = Alert()
    alerts.run_loop()


if __name__ == '__main__':
    main()

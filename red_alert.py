#!/usr/bin/python
from hashlib import md5
from time import time, sleep
import requests

HASH_PART_1 = "@Kobi*Snir-"
HASH_PART_2 = "-#iOSLinks!"
SERVER = 'http://80.179.114.130/api2/stt.php'  # gets latest feed


class Alert():
    def __init__(self):
        self.feed = self._extract_ids(self._get_feed())

    def run(self):
        while True:
            self._check_for_update()
            sleep(1)

    def _extract_ids(self, feed):
        return list(map(lambda x: x['id'], feed))

    def _check_for_update(self):
        new_feed = self._get_feed()
        updates_to_push = filter(lambda x: x['id'] not in self.feed, new_feed)
        print(self.feed)
        print(new_feed)
        self.feed = self._extract_ids(new_feed)
        for alert in updates_to_push:
            print(alert)
            self._notify(alert)

    @staticmethod
    def _notify(alert):
        print(f'new red alert at {alert["message"]} at time {alert["date"]}')

    @staticmethod
    def _get_feed():
        timestamp = int(time() * 10000)
        request_hash = md5(b"@Kobi*Snir-" + str(timestamp).encode() + b"-#iOSLinks!").hexdigest()
        result = requests.post(SERVER, data={'method': 'getFeed', 'ts': timestamp, 'hash': request_hash})
        return result.json()['feed']


def make_request_hash(timestamp):
    return md5(b"@Kobi*Snir-" + str(timestamp).encode() + b"-#iOSLinks!").hexdigest()


def check_for_update():
    timestamp = int(time() * 10000)
    request_hash = make_request_hash(timestamp)
    result = requests.post(SERVER, data={'method': 'getFeed', 'ts': timestamp, 'hash': request_hash})
    print(result.text)
    if result.json().get('feed', False):
        print(f"red alert!!!! \n at {result.json()['feed']}")


def main():
    alerts = Alert()
    alerts.run()


if __name__ == '__main__':
    main()

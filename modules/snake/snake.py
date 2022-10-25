import json
import random


def snake():
    snakes = json.load(open('./modules/snake/available_snakes.json', 'r'))
    return random.choice(snakes)


if __name__ == '__main__':
    print(snake())

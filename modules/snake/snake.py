from random import choice


def snake():
    snakes = json.load(open('available_snakes.json', 'r'))
    return choice(snakes)


if __name__ == '__main__':
    print(snake())

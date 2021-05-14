from random import choice

SNAKES = ['נחש חשמל']

def snake():
    return choice(SNAKES)

if __name__ == '__main__':
    print(snake())
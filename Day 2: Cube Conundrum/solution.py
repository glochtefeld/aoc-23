import sys
from functools import reduce

class Game(object):
    roundNum = 0
    maxCounts = {}

def parse_game(gameText):
    game = Game()
    num, text = gameText.split(':')
    game.roundNum = gameNum(num)
    game.maxCounts = parseRounds(text)
    return game

def gameNum(game):
    return int(game.split(' ')[1])


def parseRounds(game):
    print()
    print(game)
    highest = dict()
    for _round in game.split(';'):
        vals = getValues(_round)
        print(f"vals: {vals}")
        for key in vals:
            if not(highest.get(key)):
                highest[key] = vals[key]
                continue

            if highest[key] < vals[key]:
                highest[key] = vals[key]
    print(f"highest: {highest}")
    return highest


def getValues(rnd):
    pairs = [pair.strip().split(' ') for pair in rnd.split(',')]
    print(pairs)
    _round = dict()
    for ct, key in pairs:
        _round[key] = int(ct)
    return _round

def gameValue_1(gameText, **threshholds):
    game = parse_game(gameText)
    print(game.maxCounts)
    for color in threshholds:
        if not(game.maxCounts.get(color)):
            continue
        if game.maxCounts[color] > threshholds[color]:
            return 0
    return game.roundNum

def gameValue_2(gameText):
    game = parse_game(gameText)
    print(game.maxCounts)
    power = reduce(lambda x, y: x * y, game.maxCounts.values())
    return power

if __name__ == '__main__':
    _in = sys.argv[1]
    with open(_in, 'r') as infile:
        # Solution 1
        # games = [gameValue_1(line, red=12, green=13, blue=14) for line in infile]

        # Solution 2
        games = [gameValue_2(line) for line in infile]
        print(games)
        total = sum(games)
        print(total)


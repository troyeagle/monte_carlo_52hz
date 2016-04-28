import numpy
import random


class Player:

    def __init__(self, name, level, team):
        self.name = name
        self.level = level
        self.team = team

    def get_score(self):
        return self.level - 30 * 0.1 * random.random()

    def __str__(self):
        return 'Player %s belong to team %s,level %s' % (self.name, self.team, self.level)

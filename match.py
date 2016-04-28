import random
import numpy as np
from player import Player
import pandas
from pandas import DataFrame

NUM_OF_PLAYERS = 30
FULL_SCORE = 100
LEVEL_DIFF = -0.5
LOW_SCORE = FULL_SCORE + LEVEL_DIFF * NUM_OF_PLAYERS
GROUPS = 5
NUM_PER_GROUP = NUM_OF_PLAYERS / GROUPS

names = np.arange(NUM_OF_PLAYERS)
levels = np.arange(FULL_SCORE, LOW_SCORE, LEVEL_DIFF)
teams = np.arange(NUM_OF_PLAYERS) / NUM_PER_GROUP
random.shuffle(teams)
players = []

for i in range(0, NUM_OF_PLAYERS):
    players.append(Player(int(names[i]), levels[i], int(teams[i])))


def first_round(players):
    columns = ['name', 'score', 'team']
    df = DataFrame(columns=columns)
    next_round = np.empty((0, 3), int)
    to_be_decided = np.empty((0, 3), int)
    for p in players:
        player_score = {'name': p.name, 'score': p.get_score(), 'team': p.team}
        df = df.append(player_score, ignore_index=True)
    for i in range(0, GROUPS):
        df_tmp = df[df['team'] == i].sort(columns='score', ascending=False)
        next_round = np.vstack(
            [next_round, df_tmp[0:NUM_PER_GROUP / 2].index.values])
        to_be_decided = np.vstack(
            [to_be_decided, df_tmp[NUM_PER_GROUP / 2:NUM_PER_GROUP].index.values])
    to_be_decided = to_be_decided.reshape(1,15)
    print next_round
    print to_be_decided
    return next_round, to_be_decided


def fifteen_to_five(players):
    columns = ['name', 'score', 'team']
    df = DataFrame(columns=columns)
    next_round = np.empty(5, int)
    for p in players:
        player_score = {'name': p.name, 'score': p.get_score(), 'team': p.team}
        df = df.append(player_score, ignore_index=True)
    df = df.sort(columns='score', ascending=False)
    print df
    next_round = df[0:5].index.values
    print next_round

def select_players(array):
    global players
    sub_players = []
    for i in array:
        sub_players.append(players[i])
    return sub_players

def second_round(players):
# first_round(players)
# fifteen_to_five(players)

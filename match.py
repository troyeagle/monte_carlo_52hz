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

def show_group(teams):
    pass

def first_round(players):
    columns = ['name', 'score', 'team']
    df = DataFrame(columns=columns)
    next_round = np.empty((0, 3), int)
    to_be_decided = np.empty((0, 3), int)
    for p in players:
        player_score = {'name': p.name, 'score': p.get_score(), 'team': p.team}
        df = df.append(player_score, ignore_index=True)
    for i in range(0, GROUPS):
        df_tmp = df[df['team'] == i].sort_values(by='score', ascending=False)
        next_round = np.vstack(
            [next_round, df_tmp[0:NUM_PER_GROUP / 2].index.values])
        to_be_decided = np.vstack(
            [to_be_decided, df_tmp[NUM_PER_GROUP / 2:NUM_PER_GROUP].index.values])
    to_be_decided = to_be_decided.reshape(1, 15)[0]
    # print next_round
    # print to_be_decided
    return next_round, to_be_decided


def fifteen_to_five(players):
    columns = ['name', 'score', 'team']
    df = DataFrame(columns=columns)
    for p in players:
        player_score = {'name': p.name, 'score': p.get_score(), 'team': p.team}
        df = df.append(player_score, ignore_index=True)
    df = df.sort_values(by='score', ascending=False)
    next_round = df[0:5]['name'].values.astype(int).tolist()
    # print next_round
    return next_round


def select_players(array):
    global players
    sub_players = []
    for i in array:
        sub_players.append(players[i])
    return sub_players


def second_round(players):
    columns = ['name', 'score', 'team']
    df = DataFrame(columns=columns)
    next_round = np.empty((0, 1), int)
    to_be_decided = np.empty((0, 2), int)
    players.sort(key=lambda x: x.team)
    a = 0
    for p in players:
        player_score = {'name': p.name, 'score': p.get_score(
        ), 'team': p.team, 'new_team': a % GROUPS}
        df = df.append(player_score, ignore_index=True)
        a += 1
    for i in range(0, GROUPS):
        df_tmp = df[df['new_team'] == i].sort_values(
            by='score', ascending=False)
        # next_round = np.vstack([next_round, df_tmp[0:1].index.values])
        # next_round = next_round.add(df_tmp[0:1].index.values)
        next_round = np.append(next_round, df_tmp[0:1].index.values)
        to_be_decided = np.append(to_be_decided, df_tmp[1:3].index.values)
    # print next_round
    # print to_be_decided
    return next_round, to_be_decided

# first_round(players)
# fifteen_to_five(players)
#
# second_round(players)


def match():
    second_day_1, first_day_2 = first_round(players)
    # print 'First_day_2:',first_day_2
    second_day_1 = second_day_1.reshape(1, 15)[0]
    # print 'Second_day_1:',second_day_1
    second_day_1_players = select_players(second_day_1)

    first_day_2_players = select_players(first_day_2)

    second_day_2 = fifteen_to_five(first_day_2_players)
    # print 'Last 5 to second day:',second_day_2

    ten_singers, second_day_3 = second_round(second_day_1_players)
    # print 'First 5 singers:',ten_singers
    second_day_4 = np.append(second_day_2, second_day_3)
    second_day_4_players = select_players(second_day_4)
    ten_singers_2 = fifteen_to_five(second_day_4_players)

    ten_singers_total = np.append(ten_singers, ten_singers_2)
    # print 'Ten Singers:',ten_singers_total
    return ten_singers, ten_singers_2, second_day_1, second_day_2

if __name__ == '__main__':
    print teams
    most_comp_five = np.zeros(30)
    attackers = np.zeros(30)
    advance_half_in_group = np.zeros(30)
    strugglers = np.zeros(30)
    top_ten = np.zeros(30)
    for i in range(0,100):
        random.shuffle(teams)
        a,b,c,d = match()
        for j in a:
            most_comp_five[j]+=1
            top_ten[j]+=1
        for j in b:
            attackers[j]+=1
            top_ten[j]+=1
        for j in c:
            advance_half_in_group[j]+=1
        for j in d:
            strugglers[j]+=1

    print 'Most competitive five:',most_comp_five
    print 'Attackers6~10:',attackers
    print 'Advance half in group:',advance_half_in_group
    print 'Strugglers:',strugglers
    print 'Top ten:',top_ten

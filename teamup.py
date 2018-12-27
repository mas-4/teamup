#!/usr/bin/python
import argparse, yaml, math
from itertools import combinations

last_best = 100000000000


def unique_group(iterable, k, n, groups=0):
    if groups == k:
        yield []
    pool = set(iterable)
    for combination in combinations(pool, n):
        for rest in unique_group(pool.difference(combination), k, n, groups + 1):
            yield [combination, *rest]


def variance(groups):
    total_skills = [sum(player_skills[player] for player in group) for group in groups]
    return max(total_skills) - min(total_skills)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Optimize teams based on linear programming.")
    parser.add_argument('-p', '--players', required=True, action='store',
            type=str, help="The yaml player file.")
    parser.add_argument('-k', '--teamsize', required=True, action='store',
            type=int, help="The size of the teams.")
    parser.add_argument('-n', '--numteams', required=True, action='store',
            type=int, help="The number of teams.")
    args = parser.parse_args()

    players = yaml.load(open(args.players, 'rt'))

    players = sorted(players, key=lambda k: k['skill'])

    player_skills = {player['name']: player['skill'] for player in players}

    print(f"There are {len(players)} players assigned teams.")
    
    print("The optimal team assignment is:")
    for grouping in unique_group(player_skills, args.numteams, args.teamsize):
        if variance(grouping) < last_best:
            last_best = variance(grouping)
            print(f"Variance: {variance(grouping)}")
            print(grouping)

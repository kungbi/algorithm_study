import sys
from collections import defaultdict
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


class Team:
    rank_list = []
    size = 0


def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dict = defaultdict(list)
        team_count = Counter(arr)

        rank = 1
        for i in range(n):
            team = arr[i]
            if team_count[team] < 6:
                continue
            dict[team].append(rank)
            rank += 1

        win_team = -1
        win_5 = []
        win_score = float("inf")
        for key in dict.keys():
            tmp = sum(dict[key][:4])
            if win_score > tmp:
                win_score = tmp
                win_team = key
                win_5 = dict[key][4]
            elif win_score == tmp:
                if win_5 > dict[key][4]:
                    win_score = tmp
                    win_team = key
                    win_5 = dict[key][4]
        print(win_team)


solution()

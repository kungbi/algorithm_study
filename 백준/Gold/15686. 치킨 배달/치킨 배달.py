from itertools import combinations


def calc_distance(house_list, store_list):
    dis = 0
    for house in house_list:
        tmp = float("inf")
        for store in store_list:
            tmp = min(tmp, abs(house[0] - store[0]) + abs(house[1] - store[1]))
        dis += tmp
    return dis


def solution():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house_list = []
    store_list = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                house_list.append((x, y))
            elif arr[y][x] == 2:
                store_list.append((x, y))

    result = float("inf")
    for selected_store_list in combinations(store_list, M):
        dis = calc_distance(house_list, selected_store_list)
        result = min(result, dis)
    return result


print(solution())

import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)


def get_map_info(arr):
    global h, w

    map_info = dict()
    dirty_cnt = 0
    map_info["dirty_list"] = []
    for y in range(h):
        for x in range(w):
            if arr[y][x] == "o":
                map_info["start"] = (x, y)
            elif arr[y][x] == "*":
                dirty_cnt += 1
                map_info["dirty_list"].append((x, y))
    map_info["dirty_cnt"] = dirty_cnt
    return map_info


def pos2int(dirty_list, dirty_pos2int):
    i = 0

    for dirty in dirty_list:
        x, y = dirty
        dirty_pos2int[y][x] = i
        i += 1


def is_frame(x, y):
    global w, h
    return 0 <= x < w and 0 <= y < h


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def calc_dirty_dis(arr, start_pos, dirty_pos2map):
    queue = deque([[start_pos[0], start_pos[1], 0]])
    visited = [[False] * w for _ in range(h)]
    visited[start_pos[1]][start_pos[0]] = True
    dirty_pos = []

    while queue:
        curr = queue.popleft()
        x, y, d = curr
        if arr[y][x] == "*" and d != 0:
            dirty_pos.append([dirty_pos2map[y][x], d])

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_frame(nx, ny) and visited[ny][nx] == False and arr[ny][nx] != "x":
                visited[ny][nx] = True
                queue.append([nx, ny, d + 1])
    return dirty_pos


def f(curr, dirty_edges, dirty_visited, dirty_cnt, moved_cnt):
    global result

    if dirty_cnt == 0:
        result = min(result, moved_cnt)
        return

    if result <= moved_cnt:
        return

    for i in range(len(dirty_edges)):
        d = dirty_edges[curr][i]
        if d != -1 and dirty_visited[i] == False:
            dirty_visited[i] = True
            f(i, dirty_edges, dirty_visited, dirty_cnt - 1, moved_cnt + d)
            dirty_visited[i] = False


w = h = 0
result = 0


def solution():
    global w, h, result

    while True:
        w, h = map(int, input().split())
        result = float("inf")
        if w == 0 and h == 0:
            return
        arr = [list(input()) for _ in range(h)]
        map_info = get_map_info(arr)
        dirty_pos2map = [[-1] * w for _ in range(h)]
        pos2int(map_info["dirty_list"], dirty_pos2map)

        # 더러운 칸 끼리의 최소 거리 계산
        dirty_each_dis = []
        for i in range(len(map_info["dirty_list"])):
            dirty_each_dis.append(
                calc_dirty_dis(arr, map_info["dirty_list"][i], dirty_pos2map)
            )

        # 더러운 칸 끼리 거리 -> edge table
        dirty_edges = [
            [-1] * map_info["dirty_cnt"] for _ in range(map_info["dirty_cnt"])
        ]
        for i in range(map_info["dirty_cnt"]):
            for dirty in dirty_each_dis[i]:
                num, d = dirty
                dirty_edges[i][num] = d

        dirty_visited = [False] * map_info["dirty_cnt"]
        start_dirty_dis = calc_dirty_dis(arr, map_info["start"], dirty_pos2map)

        for pos in start_dirty_dis:
            dirty_visited[pos[0]] = True
            f(pos[0], dirty_edges, dirty_visited, map_info["dirty_cnt"] - 1, pos[1])
            dirty_visited[pos[0]] = False

        print(result if result != float("inf") else -1)


solution()

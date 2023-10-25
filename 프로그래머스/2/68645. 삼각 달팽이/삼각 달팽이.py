def next_pos(map, x, y, dir, n):
    if dir == 0:
        if y + 1 < n and map[y + 1][x] == 0:
            y += 1
        else:
            dir = 3
            x += 1
    elif dir == 1:
        if y - 1 >= 0 and x - 1 >= 0 and map[y - 1][x - 1] == 0:
            y -= 1
            x -= 1
        else:
            dir = 0
            y += 1
    elif dir == 3:
        if x + 1 <= y and map[y][x + 1] == 0:
            x += 1
        else:
            dir = 1
            y -= 1
            x -= 1
    return x, y, dir


def solution(n):
    map = [[0] * i for i in range(1, n + 1)]
    dir = 0
    x = 0
    y = -1
    for i in range(1, ((n * (n + 1)) // 2 + 1)):
        x, y, dir = next_pos(map, x, y, dir, n)
        map[y][x] = i

    result = []
    for i in map:
        result += i
    return result


print(solution(6))

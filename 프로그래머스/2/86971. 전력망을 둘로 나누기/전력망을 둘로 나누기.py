import sys


def bfs(wires_table, start, excep, n):
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    q = [start]
    count = 0
    while (len(q)):
        curr = q.pop(0)
        visited[curr] = 1

        for next in wires_table.get(curr, []):
            if (next != excep and visited[next] != 1):
                q.append(next)
        count += 1
    return (count)


def solution(n, wires):
    wires_table = dict()
    max_node_count = 0
    for wire in wires:
        max_node_count = max(max_node_count, wire[0], wire[1])

        if (wires_table.get(wire[0], 0) == 0):
            wires_table[wire[0]] = []
        wires_table[wire[0]].append(wire[1])
        if (wires_table.get(wire[1], 0) == 0):
            wires_table[wire[1]] = []
        wires_table[wire[1]].append(wire[0])

    min = sys.maxsize
    for wire in wires:
        x1 = bfs(wires_table, wire[0], wire[1], max_node_count)
        x2 = bfs(wires_table, wire[1], wire[0], max_node_count)
        if (abs(x1 - x2) < min):
            min = abs(x1 - x2)
    return (min)
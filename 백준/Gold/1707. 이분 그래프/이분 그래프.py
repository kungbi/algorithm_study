import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution(visited, edges):

    for start in range(1, len(visited)):
        if visited[start] != 2:
            continue
        queue = deque([(start, 0)])
        visited[start] = 0

        while queue:
            curr, color = queue.popleft()
            for n_node in edges[curr]:
                if visited[n_node] == color:
                    return False
                if visited[n_node] != 2:
                    continue
                queue.append((n_node, (color + 1) % 2))
                visited[n_node] = (color + 1) % 2
    return True


def main():
    t = int(input())
    for _ in range(t):
        V, E = map(int, input().split())
        edges = defaultdict(list)
        for _ in range(E):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)
        visited = [2] * (V + 1)
        answer = solution(visited, edges)
        print("YES" if answer else "NO")


main()

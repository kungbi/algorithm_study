import sys
from collections import defaultdict
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())

    flights = defaultdict(list)
    for _ in range(k):
        a, b, c = map(int, input().split())
        if a >= b:
            continue
        flights[a].append((b, c))

    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    dp[1][0] = 0
    queue = deque([(1, 0, 0)])

    while queue:
        node, cost, count = queue.popleft()
        if cost < dp[node][count]:
            continue
        if count == m - 1:
            continue

        for dest, n_cost in flights[node]:
            new_cost = cost + n_cost
            if new_cost <= dp[dest][count + 1]:
                continue
            dp[dest][count + 1] = new_cost
            queue.append((dest, new_cost, count + 1))
    ans = max(dp[n])
    print(0 if ans < 0 else ans)


main()

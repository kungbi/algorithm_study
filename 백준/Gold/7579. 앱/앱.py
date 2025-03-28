import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    apps_memory = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))

    max_cost = sum(costs)
    dp = [[0] * (max_cost + 1) for _ in range(n + 1)]
    answer = max_cost

    for app in range(1, n + 1):
        memory = apps_memory[app]
        curr_cost = costs[app]

        for cost in range(max_cost + 1):
            if cost >= curr_cost:
                dp[app][cost] = max(
                    dp[app - 1][cost], dp[app - 1][cost - curr_cost] + memory
                )
            else:
                dp[app][cost] = dp[app - 1][cost]

            if dp[app][cost] >= m:
                answer = min(answer, cost)

    print(answer)


main()

import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def is_available(arr, pos, time):
    if not 0 <= pos <= 100_000:
        return False

    if arr[pos] < time + 1:
        return False

    return True


def main():
    n, k = map(int, input().split())
    arr = [100_002] * 100_001

    arr[n] = 0
    queue = deque([(n, 0)])

    answer_time = float("inf")
    answer_cases = 0
    while queue:
        pos, time = queue.popleft()
        if pos == k:
            if time < answer_time:
                answer_time = time
                answer_cases = 1
            elif time == answer_time:
                answer_cases += 1
            continue

        n_pos = pos - 1
        if is_available(arr, n_pos, time):
            arr[n_pos] = time + 1
            queue.append((n_pos, arr[n_pos]))
        n_pos = pos + 1
        if is_available(arr, n_pos, time):
            arr[n_pos] = time + 1
            queue.append((n_pos, arr[n_pos]))
        n_pos = pos * 2
        if is_available(arr, n_pos, time):
            arr[n_pos] = time + 1
            queue.append((n_pos, arr[n_pos]))

    print(answer_time)
    print(answer_cases)


main()

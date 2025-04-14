def solution(arr, idx, level, m, result):
    if level == m:
        print(*result)
        return

    for i in range(idx, len(arr)):
        result.append(arr[i])
        solution(arr, i + 1, level + 1, m, result)
        result.pop()


def main():
    n, m = map(int, input().split())
    arr = [i for i in range(1, n + 1)]
    solution(arr, 0, 0, m, [])


main()

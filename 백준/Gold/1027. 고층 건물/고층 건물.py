def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    for i in range(n):
        count = 0

        min_num = float("inf")
        for j in range(i - 1, -1, -1):
            slope = (arr[j] - arr[i]) / (j - i)
            if slope < min_num:
                count += 1
                min_num = (arr[i] - arr[j]) / (i - j)

        max_num = float("-inf")
        for j in range(i + 1, n):
            slope = (arr[j] - arr[i]) / (j - i)
            if max_num < slope:
                count += 1
                max_num = slope
        answer = max(answer, count)

    print(answer)


solution()

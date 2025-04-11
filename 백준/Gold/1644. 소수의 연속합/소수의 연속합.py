import sys


def input():
    return sys.stdin.readline().rstrip()


def get_primes(n):
    arr = [True] * (n + 1)

    for i in range(2, int(n**0.5 + 1) + 1):
        for num in range(i * 2, n + 1, i):
            arr[num] = False

    result = []
    for i in range(2, n + 1):
        if arr[i] == True:
            result.append(i)
    return result


def main():
    n = int(input())

    primes = get_primes(n)
    prefix_sum = [primes[0]] if len(primes) else []
    for i in range(1, len(primes)):
        prefix_sum.append(prefix_sum[i - 1] + primes[i])

    answer = 0
    left = 0
    while left < len(primes):
        start = left
        end = len(primes) - 1
        while start <= end:
            mid = (start + end) // 2
            sum_num = prefix_sum[mid]
            if 0 < left:
                sum_num -= prefix_sum[left - 1]

            if sum_num == n:
                answer += 1
                break
            if sum_num < n:
                start = mid + 1
            else:
                end = mid - 1

        left += 1
    print(answer)


main()

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def update_tree(tree, idx, value):
    if (idx == 0):
        return
    
    tree[idx] += value
    update_tree(tree, idx // 2, value)

def make_tree(arr, N):
    tree = [0] * (4 * N)

    for i in range(N):
        tree[2 * N + i] = arr[i]

    for i in range(2 * N - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    return tree

def sum_tree(tree, l, r):
    result = 0

    while l <= r:
        if (l % 2 == 1):
            result += tree[l]
            l += 1
        if (r % 2 == 0):
            result += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return result


def main():
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    tree = make_tree(arr, N)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if (a == 1):
            idx = 2 * N + b - 1
            update_tree(tree, idx, c - tree[idx])
        if (a == 2):
            l_idx = 2 * N + b - 1
            r_idx = 2 * N + c - 1
            print(sum_tree(tree, l_idx, r_idx))

main()
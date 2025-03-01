import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

def make_tree(tree, arr, l, r, idx):
    if l == r:
        tree[idx] = arr[l - 1]
        return tree[idx]

    mid = (l + r) // 2
    tree[idx] = (make_tree(tree, arr, l, mid, idx * 2) * make_tree(tree, arr, mid + 1, r, idx * 2 + 1)) % 1_000_000_007
    return tree[idx]

def update_tree(tree, start, end, curr_idx, update_idx, value):
    if not (start <= update_idx <= end):
        return 

    if start == end:
        tree[curr_idx] = value
        return 
    
    mid = (start + end) // 2
    update_tree(tree, start, mid, curr_idx * 2, update_idx, value)
    update_tree(tree, mid + 1, end, curr_idx * 2 + 1, update_idx, value)
    tree[curr_idx] = (tree[curr_idx * 2] * tree[curr_idx * 2 + 1]) % 1_000_000_007

def mul_tree(tree, start, end, left, right, idx):
    if end < left or right < start:
        return 1
    
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    return (mul_tree(tree, start, mid, left, right, idx * 2) *
        mul_tree(tree, mid + 1, end, left, right, idx * 2 + 1)) % 1_000_000_007


def main():
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    tree = [0] * (N * 4)
    make_tree(tree, arr, 1, N, 1)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update_tree(tree, 1, N, 1, b, c)
        if a == 2:
            print(mul_tree(tree, 1, N, b, c, 1) % 1_000_000_007)


main()
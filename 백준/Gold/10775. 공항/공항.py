import sys


def input():
    return sys.stdin.readline().rstrip()


def find(disjoint_arr, idx):
    if disjoint_arr[idx] == idx:
        return disjoint_arr[idx]
    disjoint_arr[idx] = find(disjoint_arr, disjoint_arr[idx])
    return disjoint_arr[idx]


def join(disjoint_arr, a, b):
    a_parent = find(disjoint_arr, a)
    b_parent = find(disjoint_arr, b)
    if a_parent != b_parent:
        disjoint_arr[a_parent] = b_parent


def main():
    G = int(input())
    p = int(input())

    g_arr = [int(input()) for _ in range(p)]
    answer = 0

    disjoint_arr = [i for i in range(G + 1)]

    for idx in g_arr:
        found_idx = find(disjoint_arr, idx)
        if found_idx == 0:
            break

        join(disjoint_arr, idx, found_idx - 1)
        answer += 1
    print(answer)


main()

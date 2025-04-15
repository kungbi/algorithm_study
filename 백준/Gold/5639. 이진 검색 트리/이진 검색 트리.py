import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree(node):
    if node is None:
        return

    print_tree(node.left)
    print_tree(node.right)
    print(node.value)


def solution(arr, left, right):
    if left > right or len(arr) <= left:
        return
    pivot = arr[left]

    next_left = left + 1
    next_right = next_left
    for i in range(next_left, len(arr)):
        if pivot < arr[i]:
            next_right = i
            break

    solution(arr, next_left, next_right - 1)
    solution(arr, next_right, right)
    print(pivot)


def main():
    arr = []
    while True:
        try:
            num = int(input())
            arr.append(num)
        except:
            break

    solution(arr, 0, len(arr))


main()

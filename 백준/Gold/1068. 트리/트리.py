import sys


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self):
        self.partent = None
        self.children = []

    def __str__(self):
        return f"{self.partent}, {self.children}"


def count_leaf(nodes, idx):
    curr_node = nodes[idx]
    if curr_node == None:
        return 0
    if len(curr_node.children) == 0:
        return 1

    result = 0
    for child in curr_node.children:
        result += count_leaf(nodes, child)
    return result


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    delete_node = int(input())

    nodes = [Node() for _ in range(n)]
    for i in range(n):
        if arr[i] == -1:
            continue
        parent = arr[i]

        nodes[parent].children.append(i)
        nodes[i].partent = parent

    nodes[delete_node] = None
    for node in nodes:
        if node == None:
            continue
        if delete_node in node.children:
            node.children.remove(delete_node)

    root_node = None
    for i in range(n):
        if nodes[i] == None:
            continue
        if nodes[i].partent == None:
            root_node = i
            break

    if root_node == None:
        return 0

    return count_leaf(nodes, root_node)


print(main())

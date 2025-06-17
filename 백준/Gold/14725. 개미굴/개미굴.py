import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, food):
        self.food = food
        self.children = defaultdict(Node)

    def addChild(self, food):
        if food in self.children:
            return
        self.children[food] = Node(food)

    def getChild(self, food):
        return self.children[food]

    def getChildren(self):
        return self.children

    def __str__(self):
        return self.food


def print_tree(level, node):
    print("-" * level + str(node))

    items = sorted(node.getChildren().items())
    for key, node in items:
        print_tree(level + 2, node)


def main():
    n = int(input())

    tree = Node(None)
    for _ in range(n):
        foods = input().split()[1:]

        node = tree
        for food in foods:
            node.addChild(food)
            node = node.getChild(food)

    items = sorted(tree.getChildren().items())
    for key, node in items:
        print_tree(0, node)


main()

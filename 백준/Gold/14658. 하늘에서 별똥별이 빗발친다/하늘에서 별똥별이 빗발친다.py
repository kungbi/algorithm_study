import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, l, k = map(int, input().split())
    stars = [tuple(map(int, input().split())) for _ in range(k)]

    points = []
    for i in range(k):
        for j in range(k):
            points.append((stars[i][0], stars[j][1]))

    answer = float("inf")
    for point in points:
        lx = point[0]
        ly = point[1]
        rx = lx + l
        ry = ly + l

        result = 0
        for i in range(k):
            if lx <= stars[i][0] <= rx and ly <= stars[i][1] <= ry:
                result += 1
        answer = min(answer, k - result)
    print(answer)


main()

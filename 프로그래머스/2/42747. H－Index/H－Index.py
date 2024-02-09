import bisect

def solution(citations):
    citations.sort()
    n = len(citations)

    if n == 1 and 0 < citations[0]:
        return 1
    for h in range(n, -1, -1):
        x = bisect.bisect_left(citations, h)
        if h <= n - x:
            return h
    return 0
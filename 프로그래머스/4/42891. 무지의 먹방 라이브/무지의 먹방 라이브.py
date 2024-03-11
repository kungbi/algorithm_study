from heapq import heappop
from heapq import heappush


def solution(food_times, k):
    food_len = len(food_times)

    food_heap = []
    for i in range(food_len):
        heappush(food_heap, (food_times[i], i + 1))

    prev = 0
    while True:
        if not food_heap:
            return -1
        num, i = food_heap[0]
        if k - (num - prev) * food_len < 0:
            break
        heappop(food_heap)
        k -= (num - prev) * food_len
        food_len -= 1
        prev = num

    food_ids = [food[1] for food in food_heap]
    food_ids.sort()
    return food_ids[k % len(food_ids)]

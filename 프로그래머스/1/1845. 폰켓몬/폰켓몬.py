from collections import Counter

def solution(nums):
    counter = Counter(nums)
    max_k = len(counter)
    return min(len(nums)//2, max_k)
    
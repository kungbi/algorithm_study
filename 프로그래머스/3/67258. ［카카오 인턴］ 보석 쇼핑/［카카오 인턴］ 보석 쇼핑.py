import sys
from collections import defaultdict


def solution(gems):
    n = len(gems)
    k = len(set(gems))

    left = 0
    right = 0
    sum_counter = defaultdict(int)
    sum_counter[gems[0]] += 1
    answer_v = float('inf')
    answer_l = []
    while left < n and right < n:
        if len(sum_counter) != k:
            right += 1
            if right < n:
                sum_counter[gems[right]] += 1
        elif len(sum_counter) == k:
            if answer_v > right - left + 1:
                answer_v = right - left + 1
                answer_l = [left + 1, right + 1]
            sum_counter[gems[left]] -= 1
            if sum_counter[gems[left]] == 0:
                del sum_counter[gems[left]]
            left += 1
    return answer_l
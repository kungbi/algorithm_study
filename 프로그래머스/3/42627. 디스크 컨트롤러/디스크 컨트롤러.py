from heapq import heappop
from heapq import heappush


def solution(jobs):
    result = 0
    i = curr_time = 0
    start = -1
    queue = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= curr_time:
                heappush(queue, [job[1], job[0]])

        if queue:
            job_size, job_start_time = heappop(queue)
            start = curr_time
            curr_time += job_size
            result += curr_time - job_start_time
            i += 1
        else:
            curr_time += 1
    return result // len(jobs)

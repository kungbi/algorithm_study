from heapq import heappop
from heapq import heappush


def solution(jobs):
    jobs.sort(key=lambda x: x[0], reverse=True)

    job_len = len(jobs)
    result = completed_job_cnt = 0
    queue = []
    curr_time = 0
    while completed_job_cnt < job_len:
        while jobs and jobs[-1][0] <= curr_time:
            job = jobs.pop()
            heappush(queue, (job[1], job[0]))

        if queue:
            job_size, job_start_time = heappop(queue)
            curr_time += job_size
            result += curr_time - job_start_time
            completed_job_cnt += 1
        else:
            curr_time += 1

    return result // job_len

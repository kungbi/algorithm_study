def solution(elements):
    n = len(elements)
    elements *= 2
    prefix_sum = [0] * (n * 2)
    prefix_sum[0] = elements[0]
    for i in range(1, n * 2):
        prefix_sum[i] = prefix_sum[i - 1] + elements[i]

    answer = []
    c = 0
    for _ in range(n):
        for i in range(n):
            start = prefix_sum[i - 1] if 0 < i else 0
            answer.append(prefix_sum[i + c] - start)
        c += 1
    return len(set(answer))
        
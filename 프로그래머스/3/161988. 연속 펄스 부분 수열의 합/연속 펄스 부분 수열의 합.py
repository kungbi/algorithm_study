def solution(sequence):
    n = len(sequence)
    prefix_sum1 = [0] * n
    prefix_sum2 = [0] * n

    prefix_sum1[0] = sequence[0] * -1
    prefix_sum2[0] = sequence[0]

    mask = [1, -1]
    max_sum = -100_001
    if n == 1:
        return max(prefix_sum1[0], prefix_sum2[0])
    for i in range(1, n):
        if prefix_sum1[i-1] < 0:
            prefix_sum1[i-1] = 0
        prefix_sum1[i] = prefix_sum1[i-1] + sequence[i] * (mask[0])
    
        if prefix_sum2[i-1] < 0:
            prefix_sum2[i-1] = 0
        prefix_sum2[i] = prefix_sum2[i-1] + sequence[i] * (mask[1])

        max_sum = max(max_sum, prefix_sum1[i], prefix_sum2[i])
        mask.reverse()

    return max_sum


def update_result(result, a, b):
    if abs(a - b) < abs(result[0] - result[1]):
        result[0] = a
        result[1] = b
    elif abs(a - b) == abs(result[0] - result[1]):
        if a < result[0]:
            result[0] = a
            result[1] = b
def solution(sequence, k):
    prefix_sum = [0] * len(sequence)
    prefix_sum[0] = sequence[0]
    for i in range(1, len(sequence)):
        prefix_sum[i] = prefix_sum[i - 1] + sequence[i]

    result = [float('-inf'), float('inf')]
    for i in range(len(sequence)):
        left = i + 1
        right = len(sequence) - 1
        start_num = 0 if i == 0 else prefix_sum[i - 1]
        
        if prefix_sum[i] - start_num == k:
            update_result(result, i, i)
        
        while left <= right:
            mid = (left + right) // 2
            total_sum = prefix_sum[mid] - start_num
            if k < total_sum:
                right = mid - 1
            elif total_sum < k:
                left = mid + 1
            elif k == total_sum:
                if abs(i - mid) < abs(result[0] - result[1]):
                    update_result(result, i, mid)
                break
    return result

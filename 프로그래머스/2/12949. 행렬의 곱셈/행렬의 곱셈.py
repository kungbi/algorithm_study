def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp_row = []
        for l in range(len(arr2[0])):
            tmp = 0
            for j in range(len(arr1[0])):
                tmp += arr1[i][j] * arr2[j][l]
            tmp_row.append(tmp)
        answer.append(tmp_row)
    return answer
        
import sys
MAX = float('inf')


def input():
    return sys.stdin.readline().strip()

def main():
    s = input()
    n = len(s)

    palindrom_matrix = [[0] * n for _ in range(n)]
    for size in range(n):
        for i in range(n):
            if not i + size < n:
                continue

            if s[i] != s[i + size]:
                continue

            other_s = i + 1
            other_e = i + size - 1
            if other_s >= other_e or n <= other_s:
                palindrom_matrix[i][i + size] = 1
                continue
            
            if palindrom_matrix[other_s][other_e]:
                palindrom_matrix[i][i + size] = 1

    min_matrix = [MAX] * n
    min_matrix[0] = 1
    for end in range(n):
        for start in range(end + 1):
            if palindrom_matrix[start][end]:
                if 0 < start:
                    min_matrix[end] = min(min_matrix[start - 1] + 1, min_matrix[end])
                elif start == 0:
                    min_matrix[end] = min(1, min_matrix[end])
        
        if min_matrix[end] == MAX:
            min_matrix[end] = min_matrix[end - 1] + 1
    print(min_matrix[n-1])
    


main()
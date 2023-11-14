def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def sol():
    M, N = tuple(map(int, input().split()))
    for i in range(M, N + 1):
        if is_prime(i) == True:
            print(i)


sol()

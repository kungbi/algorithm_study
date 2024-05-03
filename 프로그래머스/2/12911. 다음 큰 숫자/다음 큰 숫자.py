def to_binary(n):
    binary = ""
    while n != 0:
        binary += str(n % 2)
        n //= 2
    return binary

def solution(n):
    n_one_count = to_binary(n).count("1")
    i = n
    while True:
        i += 1
        if n_one_count == to_binary(i).count("1"):
            return i
        
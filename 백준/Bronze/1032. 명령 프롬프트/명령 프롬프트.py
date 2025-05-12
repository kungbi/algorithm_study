def main():
    n = int(input())
    arr = [input() for _ in range(n)]

    for i in range(len(arr[0])):

        if all(arr[j][i] == arr[0][i] for j in range(n)):
            print(arr[0][i], end="")
        else:
            print("?", end="")


main()

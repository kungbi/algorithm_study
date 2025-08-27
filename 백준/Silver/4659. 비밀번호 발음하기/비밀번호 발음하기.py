import sys


def input():
    return sys.stdin.readline().rstrip()


def vowels_check(password):
    for c in password:
        if is_vowels(c):
            return True
    return False


def is_vowels(c):
    if c in "aeiou":
        return True
    return False


def continuously_check(password):
    for i in range(2, len(password)):
        if (
            is_vowels(password[i - 2])
            and is_vowels(password[i - 1])
            and is_vowels(password[i])
        ):
            return False
        if (
            not is_vowels(password[i - 2])
            and not is_vowels(password[i - 1])
            and not is_vowels(password[i])
        ):
            return False

        if (password[i - 2] == password[i - 1] and password[i - 1] not in "eo") or (
            password[i - 1] == password[i] and password[i] not in "eo"
        ):
            return False
    return True


def solution(password):
    if vowels_check(password) == False:
        return False
    if continuously_check(password) == False:
        return False
    return True


def main():
    while True:
        password = input()
        if password == "end":
            return
        if solution(password):
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")


main()

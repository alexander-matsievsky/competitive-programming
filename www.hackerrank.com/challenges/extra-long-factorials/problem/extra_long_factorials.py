def extra_long_factorials(n: int) -> int:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    n = int(input().strip())
    print(extra_long_factorials(n))

def staircase(n: int) -> str:
    chars: list[str] = [None] * (n * (n + 1))
    for i in range(len(chars)):
        div, mod = divmod((i + 1), (n + 1))
        if mod == 0:
            chars[i] = "\n"
        elif mod >= n - div:
            chars[i] = "#"
        else:
            chars[i] = " "
    return "".join(chars)


if __name__ == "__main__":
    n = int(input().strip())
    print(staircase(n), end="")

def plus_minus(arr: [int]) -> (float, float, float):
    positive, negative, zero = 0.0, 0.0, 0.0
    for x in arr:
        if x < 0:
            negative += 1
        if x == 0:
            zero += 1
        if x > 0:
            positive += 1
    return (
        round(positive / len(arr), 6),
        round(negative / len(arr), 6),
        round(zero / len(arr), 6),
    )


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(*plus_minus(arr), sep="\n")

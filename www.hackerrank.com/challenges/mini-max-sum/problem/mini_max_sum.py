def mini_max_sum(arr: [int]) -> (int, int):
    sum_ = 0
    for x in arr:
        sum_ += x
    minimum, maximum = sum_, -sum_
    for x in arr:
        minimum = min(minimum, sum_ - x)
        maximum = max(maximum, sum_ - x)
    return minimum, maximum


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    minimum, maximum = mini_max_sum(arr)
    print(f"{minimum} {maximum}")

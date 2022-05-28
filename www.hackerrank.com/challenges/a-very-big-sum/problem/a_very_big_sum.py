def a_very_big_sum(ar: [int]) -> int:
    sum_ = 0
    for x in ar:
        sum_ += x
    return sum_


if __name__ == "__main__":
    ar_count = int(input().strip())
    ar = list(map(int, input().strip().split()))
    print(a_very_big_sum(ar))

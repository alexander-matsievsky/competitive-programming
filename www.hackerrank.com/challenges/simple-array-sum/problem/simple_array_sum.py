def simple_array_sum(ar: [int]) -> int:
    sum_ = 0
    for x in ar:
        sum_ += x
    return sum_


if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().strip().split()))
    print(simple_array_sum(ar))

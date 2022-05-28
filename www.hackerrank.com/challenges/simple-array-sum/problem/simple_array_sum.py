def simple_array_sum(ar: [int]) -> int:
    sum = 0
    for x in ar:
        sum += x
    return sum


if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().strip().split()))
    print(simple_array_sum(ar))

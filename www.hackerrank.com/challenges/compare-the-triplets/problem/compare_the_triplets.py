def compare_triplets(a: (int, int, int), b: (int, int, int)) -> (int, int):
    points = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            points[0] += 1
        if a[i] < b[i]:
            points[1] += 1
    return tuple(points)


if __name__ == "__main__":
    a, b = compare_triplets(
        a=tuple(map(int, input().strip().split())),
        b=tuple(map(int, input().strip().split())),
    )
    print(f"{a} {b}")

def diagonal_difference(arr: [[int]]) -> int:
    left_to_right_diagonal, right_to_left_diagonal = 0, 0
    len_arr = len(arr)
    for i in range(len_arr):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][len_arr - i - 1]
    return abs(left_to_right_diagonal - right_to_left_diagonal)


if __name__ == "__main__":
    n = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    print(diagonal_difference(arr))

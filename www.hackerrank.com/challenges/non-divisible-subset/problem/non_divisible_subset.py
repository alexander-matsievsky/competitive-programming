def non_divisible_subset(k: int, s: set[int]) -> int:
    if k == 1 or len(s) == 1:
        return 1

    mod_k = [0] * k
    for x in s:
        mod_k[x % k] += 1
    subset_size = len(s)
    for i in range((mid := len(mod_k) // 2) + 1):
        if i == 0 or i == mid and i * 2 == k:
            subset_size -= max(0, mod_k[i] - 1)
        else:
            subset_size -= min(mod_k[i], mod_k[-i])
    return subset_size


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    s = set(map(int, input().strip().split()))
    print(non_divisible_subset(k, s))

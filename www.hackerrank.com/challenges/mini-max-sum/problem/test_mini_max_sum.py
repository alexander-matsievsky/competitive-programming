from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st
from mini_max_sum import mini_max_sum


def test_hackerrank():
    assert mini_max_sum([1, 2, 3, 4, 5]) == (10, 14)


@given(arr=st.lists(st.integers(1, 10**9), min_size=5, max_size=5))
def test_hypothesis(arr):
    assert mini_max_sum(arr) == (
        min(sums := [*map(sum, combinations(arr, 4))]),
        max(sums),
    )

from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st
from non_divisible_subset import non_divisible_subset


def test_hackerrank():
    assert non_divisible_subset(3, {1, 7, 2, 4}) == 3


@st.composite
def set_(draw):
    # n = draw(st.integers(1, 10**5))
    # return draw(st.sets(st.integers(1, 10**9), min_size=n, max_size=n))
    n = draw(st.integers(1, 10**1))
    return draw(st.sets(st.integers(1, 10**2), min_size=n, max_size=n))


@given(k=st.integers(1, 100), s=set_())
def test_hypothesis(k, s):
    assert non_divisible_subset(k, s) == next(
        (
            subset_size
            for subset_size in range(len(s), 0, -1)
            for subset in combinations(s, subset_size)
            if all((a + b) % k != 0 for a, b in combinations(subset, 2))
        ),
        0,
    )

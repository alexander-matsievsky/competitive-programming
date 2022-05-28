from hypothesis import given
from hypothesis import strategies as st
from simple_array_sum import simple_array_sum


def test_hackerrank():
    assert simple_array_sum([1, 2, 3, 4, 10, 11]) == 31


@given(ar=st.lists(st.integers(1, 1_000), min_size=1, max_size=1_000))
def test_hypothesis(ar):
    assert simple_array_sum(ar) == sum(ar)

from functools import reduce

from extra_long_factorials import extra_long_factorials
from hypothesis import given
from hypothesis import strategies as st


def test_hackerrank():
    assert extra_long_factorials(25) == 15511210043330985984000000


@given(n=st.integers(1, 100))
def test_hypothesis(n):
    assert extra_long_factorials(n) == reduce(lambda a, b: a * b, range(1, n + 1))

from hypothesis import given
from hypothesis import strategies as st

from . import solve_me_first


def test_hackerrank():
    assert solve_me_first(a=2, b=3) == 5


@given(a=st.integers(1, 1_000), b=st.integers(1, 1_000))
def test_hypothesis(a, b):
    assert solve_me_first(a, b) == a + b

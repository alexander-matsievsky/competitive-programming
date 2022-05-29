from hypothesis import given
from hypothesis import strategies as st
from plus_minus import plus_minus


def test_hackerrank():
    assert plus_minus([-4, 3, -9, 0, 4, 1]) == (0.500000, 0.333333, 0.166667)


@st.composite
def array(draw):
    n = draw(st.integers(1, 100))
    return draw(st.lists(st.integers(-100, 100), min_size=n, max_size=n))


@given(arr=array())
def test_hypothesis(arr):
    assert plus_minus(arr) == (
        round(sum(1 for x in arr if x > 0) / len(arr), 6),
        round(sum(1 for x in arr if x < 0) / len(arr), 6),
        round(sum(1 for x in arr if x == 0) / len(arr), 6),
    )

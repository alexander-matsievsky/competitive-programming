from a_very_big_sum import a_very_big_sum
from hypothesis import given
from hypothesis import strategies as st


def test_hackerrank():
    assert 5000000015 == a_very_big_sum(
        [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    )


@st.composite
def array(draw):
    n = draw(st.integers(1, 10))
    return draw(st.lists(st.integers(0, 10**10), min_size=n, max_size=n))


@given(array())
def test_hypothesis(ar):
    assert a_very_big_sum(ar) == sum(ar)

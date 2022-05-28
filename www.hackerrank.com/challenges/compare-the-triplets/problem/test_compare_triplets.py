from compare_triplets import compare_triplets
from hypothesis import given
from hypothesis import strategies as st


def test_hackerrank():
    assert compare_triplets(a=(1, 2, 3), b=(3, 2, 1)) == (1, 1)


@given(
    a=st.tuples(st.integers(1, 100), st.integers(1, 100), st.integers(1, 100)),
    b=st.tuples(st.integers(1, 100), st.integers(1, 100), st.integers(1, 100)),
)
def test_hypothesis(a, b):
    assert compare_triplets(a, b) == (
        sum(a_ > b_ for a_, b_ in zip(a, b)),
        sum(a_ < b_ for a_, b_ in zip(a, b)),
    )

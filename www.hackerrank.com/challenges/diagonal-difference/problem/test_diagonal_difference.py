from diagonal_difference import diagonal_difference
from hypothesis import given
from hypothesis import strategies as st


def test_hackerrank():
    assert 15 == diagonal_difference(
        [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    )


@st.composite
def matrix(draw):
    n = draw(st.integers(0, 20))
    return [
        draw(st.lists(st.integers(-100, 100), min_size=n, max_size=n)) for _ in range(n)
    ]


@given(arr=matrix())
def test_hypothesis(arr):
    arr_flipped = [[*reversed(r)] for r in arr]
    assert diagonal_difference(arr) == abs(
        sum(arr[i][j] for i in range(len(arr)) for j in range(len(arr[i])) if i == j)
        - sum(
            arr_flipped[i][j]
            for i in range(len(arr_flipped))
            for j in range(len(arr_flipped[i]))
            if i == j
        )
    )

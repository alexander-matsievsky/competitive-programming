import inspect

from hypothesis import given
from hypothesis import strategies as st
from staircase import staircase


def test_hackerrank():
    assert staircase(6).rstrip() == inspect.cleandoc(
        """
             #
            ##
           ###
          ####
         #####
        ######
        """
    )


@given(n=st.integers(1, 100))
def test_hypothesis(n):
    assert staircase(n) == "".join(
        ("#" * i).rjust(n, " ") + "\n" for i in range(1, n + 1)
    )

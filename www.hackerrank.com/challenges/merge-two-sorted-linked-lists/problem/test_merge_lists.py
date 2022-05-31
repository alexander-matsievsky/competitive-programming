from hypothesis import given
from hypothesis import strategies as st
from merge_lists import SinglyLinkedList, merge_lists


def test_hackerrank():
    singly_linked_list = merge_lists(
        SinglyLinkedList.from_elements([1, 2, 3]),
        SinglyLinkedList.from_elements([3, 4]),
    )
    assert [*singly_linked_list] == [1, 2, 3, 3, 4]


@st.composite
def sorted_list(draw):
    return [*sorted(draw(st.lists(st.integers(1, 1_000), min_size=1, max_size=1_000)))]


@given(left=sorted_list(), right=sorted_list())
def test_hypothesis(left: list[int], right: list[int]):
    singly_linked_list = merge_lists(
        SinglyLinkedList.from_elements(left),
        SinglyLinkedList.from_elements(right),
    )
    assert [*singly_linked_list] == [*sorted([*left, *right])]

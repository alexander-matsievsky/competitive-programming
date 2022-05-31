from delete_duplicate_value_nodes_from_a_sorted_linked_list import SinglyLinkedList
from hypothesis import given
from hypothesis import strategies as st


def test_hackerrank():
    singly_linked_list = SinglyLinkedList.from_elements([1, 2, 2, 3, 4])
    singly_linked_list.remove_duplicates()
    assert [*singly_linked_list] == [1, 2, 3, 4]


@st.composite
def sorted_list(draw):
    return [*sorted(draw(st.lists(st.integers(1, 1_000), min_size=1, max_size=1_000)))]


@given(list_=sorted_list())
def test_hypothesis(list_):
    singly_linked_list = SinglyLinkedList.from_elements(list_)
    singly_linked_list.remove_duplicates()
    assert [*singly_linked_list] == [*sorted(set(list_))]

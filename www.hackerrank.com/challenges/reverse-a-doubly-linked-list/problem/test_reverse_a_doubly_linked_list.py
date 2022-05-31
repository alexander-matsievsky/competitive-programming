from hypothesis import given
from hypothesis import strategies as st
from reverse_a_doubly_linked_list import DoublyLinkedList


def test_hackerrank():
    doubly_linked_list = DoublyLinkedList.from_elements([1, 2, 3, 4])
    doubly_linked_list.reverse()
    assert [*doubly_linked_list] == [4, 3, 2, 1]


@given(list_=st.lists(st.integers(0, 1_000), min_size=0, max_size=1_000))
def test_hypothesis(list_):
    doubly_linked_list = DoublyLinkedList.from_elements(list_)
    doubly_linked_list.reverse()
    assert [*doubly_linked_list] == [*reversed(list_)]

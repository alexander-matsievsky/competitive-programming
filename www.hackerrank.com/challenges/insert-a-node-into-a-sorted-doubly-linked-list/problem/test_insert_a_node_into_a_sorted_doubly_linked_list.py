from hypothesis import given
from hypothesis import strategies as st
from insert_a_node_into_a_sorted_doubly_linked_list import DoublyLinkedList


def test_hackerrank():
    list_, data = [1, 3, 4, 10], 5
    doubly_linked_list = DoublyLinkedList.from_elements(list_)
    doubly_linked_list.sorted_insert(data)
    assert [*doubly_linked_list] == [1, 3, 4, 5, 10]


@st.composite
def sorted_list(draw):
    return [*sorted(draw(st.lists(st.integers(1, 1_000), min_size=1, max_size=1_000)))]


@given(list_=sorted_list(), data=st.integers(1, 1_000))
def test_hypothesis(list_, data):
    doubly_linked_list = DoublyLinkedList.from_elements(list_)
    doubly_linked_list.sorted_insert(data)
    assert [*doubly_linked_list] == [*sorted([*list_, data])]

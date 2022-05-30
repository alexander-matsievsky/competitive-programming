from hypothesis import given
from hypothesis import strategies as st
from reverse import SinglyLinkedList


def test_hackerrank():
    list_ = [1, 2, 3, 4, 5]
    singly_linked_list = SinglyLinkedList.from_elements(list_)
    singly_linked_list.reverse()
    assert [*singly_linked_list] == [5, 4, 3, 2, 1]


@given(list_=st.lists(st.integers(1, 1_000), min_size=1, max_size=1_000))
def test_hypothesis(list_):
    singly_linked_list = SinglyLinkedList.from_elements(list_)
    singly_linked_list.reverse()
    assert [*singly_linked_list] == list_[::-1]

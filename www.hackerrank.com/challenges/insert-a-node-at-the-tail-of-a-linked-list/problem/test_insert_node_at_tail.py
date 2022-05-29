from hypothesis import given
from hypothesis import strategies as st
from insert_node_at_tail import SinglyLinkedList


def test_hackerrank():
    data = [141, 302, 164, 530, 474]
    singly_linked_list = SinglyLinkedList()
    for datum in data:
        singly_linked_list.insert_node_at_tail(data=datum)
    assert [*singly_linked_list] == data


@st.composite
def list_(draw):
    n = draw(st.integers(1, 1_000))
    return draw(st.lists(st.integers(1, 1_000), min_size=n, max_size=n))


@given(data=list_())
def test_hypothesis(data):
    singly_linked_list = SinglyLinkedList()
    for datum in data:
        singly_linked_list.insert_node_at_tail(data=datum)
    assert [*singly_linked_list] == data

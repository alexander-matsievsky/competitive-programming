from hypothesis import given
from hypothesis import strategies as st
from insert_node_at_position import SinglyLinkedList


def test_hackerrank():
    head, data, position = [16, 13, 7], 1, 2
    singly_linked_list = SinglyLinkedList.from_elements(head)
    singly_linked_list.insert_node_at_position(data=data, position=position)
    assert [*singly_linked_list] == [16, 13, 1, 7]


@st.composite
def list_(draw):
    n = draw(st.integers(1, 1_000))
    head = draw(st.lists(st.integers(1, 1_000), min_size=n, max_size=n))
    data = draw(st.integers(1, 1_000))
    position = draw(st.integers(0, n))
    return head, data, position


@given(list_())
def test_hypothesis(_):
    head, data, position = _
    singly_linked_list = SinglyLinkedList.from_elements(head)
    singly_linked_list.insert_node_at_position(data=data, position=position)
    assert [*singly_linked_list] == [*head[:position], data, *head[position:]]

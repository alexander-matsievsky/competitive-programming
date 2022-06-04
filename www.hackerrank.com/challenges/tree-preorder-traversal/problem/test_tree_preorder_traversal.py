from hypothesis import given
from hypothesis import strategies as st
from tree_preorder_traversal import BinarySearchTree


def pre_order(node: BinarySearchTree):
    if not node.data:
        return
    yield node.data
    if node.left:
        yield from pre_order(node.left)
    if node.right:
        yield from pre_order(node.right)


def test_hackerrank():
    list_ = [1, 2, 5, 3, 4, 6]
    binary_search_tree = BinarySearchTree.from_elements(list_)
    assert [*binary_search_tree.pre_order()] == [1, 2, 5, 3, 4, 6]


@given(list_=st.lists(st.integers(1, 1_000), min_size=1, max_size=500))
def test_hypothesis(list_):
    binary_search_tree = BinarySearchTree.from_elements(list_)
    assert [*binary_search_tree.pre_order()] == [*pre_order(binary_search_tree)]

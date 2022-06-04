from hypothesis import given
from hypothesis import strategies as st
from tree_postorder_traversal import BinarySearchTree


def post_order(node: BinarySearchTree):
    if not node.data:
        return
    if node.left:
        yield from post_order(node.left)
    if node.right:
        yield from post_order(node.right)
    yield node.data


def test_hackerrank():
    list_ = [1, 2, 5, 3, 4, 6]
    binary_search_tree = BinarySearchTree.from_elements(list_)
    assert [*binary_search_tree.post_order()] == [4, 3, 6, 5, 2, 1]


@given(list_=st.lists(st.integers(1, 1_000), min_size=1, max_size=500))
def test_hypothesis(list_):
    binary_search_tree = BinarySearchTree.from_elements(list_)
    assert [*binary_search_tree.post_order()] == [*post_order(binary_search_tree)]

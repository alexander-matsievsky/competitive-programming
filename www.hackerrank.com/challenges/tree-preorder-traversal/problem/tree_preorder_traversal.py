from dataclasses import dataclass


@dataclass
class BinarySearchTree:
    data: int = None
    left: "BinarySearchTree" = None
    right: "BinarySearchTree" = None

    @classmethod
    def from_elements(cls, elements) -> "BinarySearchTree":
        elements = iter(elements)
        binary_search_tree = cls(next(elements, None))
        for element in elements:
            cursor, insert = binary_search_tree, BinarySearchTree(element)
            while cursor:
                if insert.data < cursor.data and not cursor.left:
                    cursor.left = insert
                    break
                if insert.data < cursor.data and cursor.left:
                    cursor = cursor.left
                if insert.data >= cursor.data and not cursor.right:
                    cursor.right = insert
                    break
                if insert.data >= cursor.data and cursor.right:
                    cursor = cursor.right
        return binary_search_tree

    def pre_order(self):
        stack = [self]
        while stack:
            cursor = stack.pop()
            cursor.right and stack.append(cursor.right)
            cursor.left and stack.append(cursor.left)
            yield cursor.data


if __name__ == "__main__":
    t = int(input().strip())
    arr = list(map(int, input().strip().split()))
    binary_search_tree = BinarySearchTree.from_elements(arr)
    print(*binary_search_tree.pre_order(), sep=" ")
    exit(0)

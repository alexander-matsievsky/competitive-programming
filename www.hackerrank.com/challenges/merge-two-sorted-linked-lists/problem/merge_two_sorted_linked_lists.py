from dataclasses import dataclass


@dataclass
class SinglyLinkedList:
    data: int = None
    next: "SinglyLinkedList" = None

    @classmethod
    def from_elements(cls, elements):
        elements = iter(elements)
        cursor = singly_linked_list = cls(next(elements, None))
        for element in elements:
            cursor.next = cls(element)
            cursor = cursor.next
        return singly_linked_list

    def __iter__(self):
        cursor = self
        while cursor and cursor.data is not None:
            yield cursor.data
            cursor = cursor.next


def merge_lists(left: SinglyLinkedList, right: SinglyLinkedList) -> SinglyLinkedList:
    cursor = singly_linked_list = SinglyLinkedList()
    while left and left.data is not None or right and right.data is not None:
        if (left and left.data is not None) and (
            not (right and right.data is not None) or left.data <= right.data
        ):
            cursor.next = SinglyLinkedList(left.data)
            left = left.next
        elif (right and right.data is not None) and (
            not (left and left.data is not None) or right.data <= left.data
        ):
            cursor.next = SinglyLinkedList(right.data)
            right = right.next
        cursor = cursor.next
    if singly_linked_list.data is None and singly_linked_list.next is not None:
        singly_linked_list = singly_linked_list.next
    return singly_linked_list


if __name__ == "__main__":
    for t in range(int(input().strip())):
        left = SinglyLinkedList.from_elements(
            int(input().strip()) for n in range(int(input().strip()))
        )
        right = SinglyLinkedList.from_elements(
            int(input().strip()) for n in range(int(input().strip()))
        )
        singly_linked_list = merge_lists(left, right)
        print(*singly_linked_list, sep=" ")
    exit(0)

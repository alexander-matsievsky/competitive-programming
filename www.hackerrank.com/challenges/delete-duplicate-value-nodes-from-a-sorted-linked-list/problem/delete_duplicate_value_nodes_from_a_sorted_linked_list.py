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

    def remove_duplicates(self):
        cursor = self
        while cursor and cursor.data is not None:
            while cursor.next and cursor.data == cursor.next.data:
                cursor.next = cursor.next.next
            cursor = cursor.next

    def __iter__(self):
        cursor = self
        while cursor and cursor.data is not None:
            yield cursor.data
            cursor = cursor.next


if __name__ == "__main__":
    for t in range(int(input().strip())):
        singly_linked_list = SinglyLinkedList.from_elements(
            int(input().strip()) for n in range(int(input().strip()))
        )
        singly_linked_list.remove_duplicates()
        print(*singly_linked_list, sep=" ")
    exit(0)

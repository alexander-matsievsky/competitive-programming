from dataclasses import dataclass


@dataclass
class DoublyLinkedList:
    data: int = None
    next: "DoublyLinkedList" = None
    prev: "DoublyLinkedList" = None

    @classmethod
    def from_elements(cls, elements) -> "DoublyLinkedList":
        elements = iter(elements)
        cursor = doubly_linked_list = cls(next(elements, None))
        for element in elements:
            cursor.next = cls(data=element, prev=cursor)
            cursor = cursor.next
        return doubly_linked_list

    def reverse(self):
        cursor = DoublyLinkedList(self.data, self.next, self.prev)
        end = cursor
        if cursor.next:
            cursor.next.prev = cursor
        while cursor:
            cursor.next, cursor.prev = cursor.prev, cursor.next
            cursor, end = cursor.prev, cursor.prev or cursor
        self.data, self.next, self.prev = end.data, end.next, end.prev

    def __iter__(self):
        cursor = self
        while cursor and cursor.data is not None:
            yield cursor.data
            cursor = cursor.next


if __name__ == "__main__":
    for t in range(int(input().strip())):
        doubly_linked_list = DoublyLinkedList.from_elements(
            int(input().strip()) for n in range(int(input().strip()))
        )
        doubly_linked_list.reverse()
        print(*doubly_linked_list, sep=" ")
    exit(0)

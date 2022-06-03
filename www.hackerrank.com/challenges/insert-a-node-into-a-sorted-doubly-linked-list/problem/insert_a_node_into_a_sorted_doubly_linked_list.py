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

    def sorted_insert(self, data: int):
        if self.data is None:
            self.data = data
            return
        cursor, insert = self, DoublyLinkedList(data=data)
        while cursor:
            if insert.data < cursor.data and not cursor.prev:
                self.data, insert.data = insert.data, self.data
                self.next, insert.next = insert, self.next
                self.prev, insert.prev = None, self
                break
            if insert.data < cursor.data and cursor.prev:
                cursor.prev.next, insert.prev = insert, cursor.prev
                cursor.prev, insert.next = insert, cursor
                break
            if insert.data >= cursor.data and not cursor.next:
                cursor.next, insert.prev = insert, cursor
                break
            cursor = cursor.next

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
        doubly_linked_list.sorted_insert(int(input().strip()))
        print(*doubly_linked_list, sep=" ")
    exit(0)

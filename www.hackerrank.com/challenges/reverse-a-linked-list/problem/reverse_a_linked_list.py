from dataclasses import dataclass


@dataclass
class SinglyLinkedList:
    data: int = None
    next: "SinglyLinkedList" = None

    @classmethod
    def from_elements(cls, elements):
        elements = iter(elements)
        node = singly_linked_list = cls(data=next(elements, None))
        for element in elements:
            node.next = cls(data=element)
            node = node.next
        return singly_linked_list

    def reverse(self):
        prev, node = None, SinglyLinkedList(data=self.data, next=self.next)
        while node.next is not None:
            node_next, node.next = node.next, prev
            prev, node = node, node_next
        self.data = node.data
        self.next = prev

    def __iter__(self):
        node = self
        if node.data is not None:
            yield node.data
        while node.next is not None:
            node = node.next
            if node.data is not None:
                yield node.data


if __name__ == "__main__":
    for t in range(int(input().strip())):
        singly_linked_list = SinglyLinkedList.from_elements(
            int(input().strip()) for n in range(int(input().strip()))
        )
        singly_linked_list.reverse()
        print(*singly_linked_list, sep=" ")
    exit(0)

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

    def insert_node_at_position(self, data: int, position: int):
        if self.data is None:
            self.data = data
            return

        node_prev, node = None, self
        for _ in range(position):
            node_prev, node = node, node.next
        if node_prev is None:
            node.data, node.next = data, SinglyLinkedList(data=node.data, next=node.next)
        else:
            node_prev.next = SinglyLinkedList(data=data, next=node)

    def __iter__(self):
        node = self
        if node.data is not None:
            yield node.data
        while node.next is not None:
            node = node.next
            if node.data is not None:
                yield node.data


if __name__ == "__main__":
    n = int(input().strip())
    singly_linked_list = SinglyLinkedList.from_elements(
        int(input().strip()) for i in range(n)
    )
    singly_linked_list.insert_node_at_position(
        data=int(input().strip()), position=int(input().strip())
    )
    print(*singly_linked_list, sep=" ")
    exit(0)

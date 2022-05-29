from dataclasses import dataclass


@dataclass
class SinglyLinkedList:
    data: int = None
    next: "SinglyLinkedList" = None

    def insert_node_at_tail(self, data: int):
        node = self
        if node.data is None:
            node.data = data
            return
        while node.next is not None:
            node = node.next
        node.next = SinglyLinkedList(data=data)

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
    singly_linked_list = SinglyLinkedList()
    for _ in range(n):
        singly_linked_list.insert_node_at_tail(int(input().strip()))
    print(*singly_linked_list, sep="\n")
    exit(0)

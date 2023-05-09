class nodes:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singly_linked_lists:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        nodes = self.head
        while nodes:
            yield nodes
            nodes = nodes.next

sl_list = singly_linked_lists()
node1 = nodes(1)
node2 = nodes(2)
singly_linked_lists.head = node1
singly_linked_lists.head.next = node2
singly_linked_lists.tail = node2

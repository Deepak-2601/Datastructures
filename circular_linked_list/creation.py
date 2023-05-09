class nodes:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class circular_single_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        nodes = self.head
        while nodes:
            yield nodes
            if nodes.next == self.head:
                break
            nodes = nodes.next

    def creating_circular_linked_list(self, node_value):
        Nodes = nodes(node_value)
        Nodes.next = Nodes
        self.head = Nodes
        self.tail = Nodes
        return "The CSLL is created"


circularsll = circular_single_linked_list()
circularsll.creating_circular_linked_list(1)
print([Node.value for Node in circularsll])

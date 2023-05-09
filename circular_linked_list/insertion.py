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

    def inserting_nodes(self, value, location):
        if self.head is None:
            return "Head is none"
        else:
            newNode = nodes(value)
            


circularsll = circular_single_linked_list()
circularsll.inserting_nodes(1,0)
circularsll.inserting_nodes(2,1)
circularsll.inserting_nodes(3,3)
circularsll.inserting_nodes(4,4)
print([Node.value for Node in circularsll])

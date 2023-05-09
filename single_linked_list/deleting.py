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

    def insertion(self, value, location):
        new_node = nodes(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                t_node = self.head
                index = 0
                while index < location - 1:
                    t_node = t_node.next
                    index += 1
                next_nodes = t_node.next
                t_node.next = new_node
                new_node.next = next_nodes
                if t_node == self.tail:
                  self.tail = new_node

    def deleting(self,loc):
        if self.head is None:
            print("linked list does not exist")
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loc == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    Nodes = self.head
                    while Nodes is not None:
                        if Nodes.next == self.tail:
                            break
                        Nodes = Nodes.next
                    Nodes.next = None
                    self.tail = None
            else:
                temp = self.head
                index = 0
                while index < loc - 1:
                    temp = temp.next
                    index += 1
                n_node = temp.next
                temp.next = n_node.next
    def deleting_completesll(self):
        if self.head is None:
            print("Sorry linked list does not exist")
        else:
            self.head = None
            self.tail = None



sl_list = singly_linked_lists()
sl_list.insertion(1, 0)
sl_list.insertion(2, 1)
sl_list.insertion(3, 2)
sl_list.insertion(4, 3)
sl_list.insertion(5, 4)
sl_list.insertion(6, 5)
#sl_list.deleting(3)
print([nodes.value for nodes in sl_list])
sl_list.deleting_completesll()
print([nodes.value for nodes in sl_list])
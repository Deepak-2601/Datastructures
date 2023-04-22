class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        newnode = Node(value)
        if self.first is None:
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        tempo = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            tempo.next = None
        self.length -= 1
        return tempo.value


queueprint = Queue(10)
queueprint.enqueue(20)

print(queueprint.dequeue())
print(queueprint.dequeue())
print(queueprint.dequeue())
class node:
    def __init__(self, values):
        self.values = values
        self.next = None

class Queue:
    def __init__(self, values):
        newnode = node(values)
        self.first = newnode
        self.last = newnode
        self.length = 1

    def enqueue(self, value):
        newnode = node(value)
        if self.first is None:
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.length = +1

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
        return tempo.values


    def printlist(self):
        tempo = self.first
        while tempo is not None:
            print(tempo.values)
            tempo = tempo.next


queueprint = Queue(89)
queueprint.enqueue(10)
print(queueprint.dequeue())
print(queueprint.dequeue())
print(queueprint.dequeue())



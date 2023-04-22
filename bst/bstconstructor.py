class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def minvaluenode(self,tempo):
        while tempo.left is not None:
            tempo = tempo.left
        return tempo


ourBST = BST()
ourBST.insert(10)
ourBST.insert(25)
ourBST.insert(44)
ourBST.insert(90)
ourBST.insert(33)
ourBST.insert(11)
ourBST.insert(67)
print(ourBST.minvaluenode(ourBST.root))
print(ourBST.minvaluenode(ourBST.root.right))



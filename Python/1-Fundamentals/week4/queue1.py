class Node:
    """
        temp
    """

    def __init__(self, value):
        self.value = value
        self.next = None

# Doc


class Queue:
    """
        temp
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0
    
    """
        temp
    """
    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node

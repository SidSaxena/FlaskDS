class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self) -> None:
        self.top = None

    def peek(self):
        return self.top
    
    def push(self, data):
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self, data):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top_next_node
        return Node
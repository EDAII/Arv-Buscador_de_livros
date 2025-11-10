class Node:
    def __init__(self, key, data, color="RED"):
        self.key = key
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

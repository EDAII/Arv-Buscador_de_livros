from .node import Node

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(None, None, "BLACK")
        self.root = self.NULL

    # ---------------------------------------------------------
    # Inserção
    # ---------------------------------------------------------
    def insert(self, key, data):
        new_node = Node(key, data)
        new_node.left = self.NULL
        new_node.right = self.NULL

        parent = None
        current = self.root

        # Inserção normal de BST
        while current != self.NULL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"

        self.fix_insert(new_node)

    # ---------------------------------------------------------
    # Ajuste da árvore após inserção
    # ---------------------------------------------------------
    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right

                # Caso 1 - tio vermelho
                if uncle.color == "RED":
                    k.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent

                else:
                    # Caso 2 - rotação dupla
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)

                    # Caso 3 - rotação simples
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                uncle = k.parent.parent.left

                if uncle.color == "RED":
                    k.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)

                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)

        self.root.color = "BLACK"

    # ---------------------------------------------------------
    # ROTAÇÕES
    # ---------------------------------------------------------
    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # ---------------------------------------------------------
    # Busca
    # ---------------------------------------------------------
    def search(self, key):
        current = self.root
        while current != self.NULL:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

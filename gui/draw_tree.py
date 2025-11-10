import tkinter as tk

class JanelaArvore:
    def __init__(self, root, arvore):
        self.root = root
        self.arvore = arvore

        self.window = tk.Toplevel(root)
        self.window.title("Visualização da Árvore Rubro-Negra")

        self.canvas = tk.Canvas(self.window, width=900, height=600, bg="white")
        self.canvas.pack()

        self.desenhar(self.arvore.root, 450, 50, 200)

    def desenhar(self, node, x, y, dx):
        if node is None or node.key is None:
            return

        # cor do nó
        fill = "red" if node.color == "RED" else "black"
        text_color = "white"

        # desenha nó
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=fill)
        self.canvas.create_text(x, y, text=node.key, fill=text_color)

        # desenha filhos
        if node.left and node.left.key is not None:
            self.canvas.create_line(x, y, x-dx, y+80)
            self.desenhar(node.left, x-dx, y+80, dx // 2)

        if node.right and node.right.key is not None:
            self.canvas.create_line(x, y, x+dx, y+80)
            self.desenhar(node.right, x+dx, y+80, dx // 2)

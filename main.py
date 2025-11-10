from data.livros_exemplo import livros_exemplo
from arvore.red_black_tree import RedBlackTree
import tkinter as tk
from gui.janela_principal import JanelaPrincipal

if __name__ == "__main__":
    arvore = RedBlackTree()

    # inserir exemplos automaticamente
    for livro in livros_exemplo:
        arvore.insert(livro["isbn"], livro)

    root = tk.Tk()
    JanelaPrincipal(root, arvore)
    root.mainloop()

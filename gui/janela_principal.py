import tkinter as tk
from .form_adicionar import FormAdicionar
from .form_buscar import FormBuscar
from .draw_tree import JanelaArvore

class JanelaPrincipal:
    def __init__(self, root, arvore):
        self.root = root
        self.arvore = arvore

        root.title("Biblioteca com Árvore Rubro-Negra")

        tk.Button(root, text="Adicionar Livro",
                  width=30,
                  command=lambda: FormAdicionar(self.root, self.arvore)).pack(pady=10)

        tk.Button(root, text="Buscar Livro",
                  width=30,
                  command=lambda: FormBuscar(self.root, self.arvore)).pack(pady=10)

        tk.Button(root, text="Mostrar Árvore",
                  width=30,
                  command=lambda: JanelaArvore(self.root, self.arvore)).pack(pady=10)

import tkinter as tk
from tkinter import ttk
from .form_adicionar import FormAdicionar
from .form_buscar import FormBuscar
from .draw_tree import JanelaArvore

class JanelaPrincipal:
    def __init__(self, root, arvore):
        self.root = root
        self.arvore = arvore

        root.title("Biblioteca com Árvore Rubro-Negra")
        root.geometry("360x240")
        root.resizable(False, False)

        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('TButton', font=('Segoe UI', 11), padding=8)
        style.configure('TLabel', font=('Segoe UI', 12))

        main_frame = ttk.Frame(root, padding=16)
        main_frame.pack(fill='both', expand=True)

        ttk.Label(main_frame, text="Biblioteca", anchor='center', font=('Segoe UI', 14, 'bold')).pack(pady=(0,10))

        ttk.Button(main_frame, text="Adicionar Livro",
                   width=30,
                   command=lambda: FormAdicionar(self.root, self.arvore)).pack(pady=6)

        ttk.Button(main_frame, text="Buscar Livro",
                   width=30,
                   command=lambda: FormBuscar(self.root, self.arvore)).pack(pady=6)

        ttk.Button(main_frame, text="Mostrar Árvore",
                   width=30,
                   command=lambda: JanelaArvore(self.root, self.arvore)).pack(pady=6)

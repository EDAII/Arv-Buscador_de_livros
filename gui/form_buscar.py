import tkinter as tk
from tkinter import messagebox

class FormBuscar:
    def __init__(self, root, arvore):
        self.arvore = arvore

        self.window = tk.Toplevel(root)
        self.window.title("Buscar Livro")

        tk.Label(self.window, text="ISBN:").pack()
        self.isbn_entry = tk.Entry(self.window)
        self.isbn_entry.pack()

        tk.Button(self.window, text="Buscar",
                  command=self.buscar).pack(pady=10)

    def buscar(self):
        isbn = self.isbn_entry.get()
        node = self.arvore.search(isbn)

        if node:
            livro = node.data
            messagebox.showinfo("Resultado",
                                f"Título: {livro['titulo']}\n"
                                f"Autor: {livro['autor']}\n"
                                f"Ano: {livro['ano']}")
        else:
            messagebox.showerror("Erro", "Livro não encontrado.")

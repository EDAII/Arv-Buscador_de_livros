import tkinter as tk
from tkinter import messagebox

class FormAdicionar:
    def __init__(self, root, arvore):
        self.arvore = arvore

        self.window = tk.Toplevel(root)
        self.window.title("Adicionar Livro")

        tk.Label(self.window, text="ISBN:").pack()
        self.isbn_entry = tk.Entry(self.window)
        self.isbn_entry.pack()

        tk.Label(self.window, text="Título:").pack()
        self.titulo_entry = tk.Entry(self.window)
        self.titulo_entry.pack()

        tk.Label(self.window, text="Autor:").pack()
        self.autor_entry = tk.Entry(self.window)
        self.autor_entry.pack()

        tk.Label(self.window, text="Ano:").pack()
        self.ano_entry = tk.Entry(self.window)
        self.ano_entry.pack()

        tk.Button(self.window, text="Adicionar",
                  command=self.adicionar).pack(pady=10)

    def adicionar(self):
        isbn = self.isbn_entry.get()
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()

        if not isbn or not titulo:
            messagebox.showerror("Erro", "ISBN e Título são obrigatórios!")
            return

        dados = {"titulo": titulo, "autor": autor, "ano": ano}

        self.arvore.insert(isbn, dados)

        messagebox.showinfo("OK", "Livro adicionado com sucesso!")
        self.window.destroy()

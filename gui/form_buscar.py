import tkinter as tk
from tkinter import messagebox, ttk

class FormBuscar:
    def __init__(self, root, arvore):
        self.arvore = arvore

        self.window = tk.Toplevel(root)
        self.window.title("Buscar Livro")
        self.window.resizable(False, False)

        self._center_window(self.window, 320, 140)

        container = ttk.Frame(self.window, padding=12)
        container.pack(fill='both', expand=True)

        ttk.Label(container, text="ISBN:").grid(row=0, column=0, sticky='w')
        self.isbn_entry = ttk.Entry(container)
        self.isbn_entry.grid(row=0, column=1, padx=(6,0), sticky='ew')

        container.columnconfigure(1, weight=1)

        ttk.Button(container, text="Buscar",
                   command=self.buscar).grid(row=1, column=0, columnspan=2, pady=(10,0))

        self.isbn_entry.focus_set()

    def _center_window(self, win, w, h):
        win.update_idletasks()
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry(f"{w}x{h}+{x}+{y}")

    def buscar(self):
        isbn = self.isbn_entry.get().strip()
        node = self.arvore.search(isbn)

        if node:
            livro = node.data
            messagebox.showinfo("Resultado",
                                f"Título: {livro['titulo']}\n"
                                f"Autor: {livro['autor']}\n"
                                f"Ano: {livro['ano']}")
        else:
            messagebox.showerror("Erro", "Livro não encontrado.")
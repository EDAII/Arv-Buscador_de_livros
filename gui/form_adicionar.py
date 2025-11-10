import tkinter as tk
from tkinter import messagebox, ttk

class FormAdicionar:
    def __init__(self, root, arvore):
        self.arvore = arvore

        self.window = tk.Toplevel(root)
        self.window.title("Adicionar Livro")
        self.window.resizable(False, False)

        self._center_window(self.window, 360, 260)

        container = ttk.Frame(self.window, padding=12)
        container.pack(fill='both', expand=True)

        ttk.Label(container, text="ISBN:").grid(row=0, column=0, sticky='w', pady=4)
        self.isbn_entry = ttk.Entry(container)
        self.isbn_entry.grid(row=0, column=1, pady=4, sticky='ew')

        ttk.Label(container, text="Título:").grid(row=1, column=0, sticky='w', pady=4)
        self.titulo_entry = ttk.Entry(container)
        self.titulo_entry.grid(row=1, column=1, pady=4, sticky='ew')

        ttk.Label(container, text="Autor:").grid(row=2, column=0, sticky='w', pady=4)
        self.autor_entry = ttk.Entry(container)
        self.autor_entry.grid(row=2, column=1, pady=4, sticky='ew')

        ttk.Label(container, text="Ano:").grid(row=3, column=0, sticky='w', pady=4)
        self.ano_entry = ttk.Entry(container)
        self.ano_entry.grid(row=3, column=1, pady=4, sticky='ew')

        container.columnconfigure(1, weight=1)

        ttk.Button(container, text="Adicionar",
                   command=self.adicionar).grid(row=4, column=0, columnspan=2, pady=(10,0))

        self.isbn_entry.focus_set()

    def _center_window(self, win, w, h):
        win.update_idletasks()
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry(f"{w}x{h}+{x}+{y}")

    def adicionar(self):
        isbn = self.isbn_entry.get().strip()
        titulo = self.titulo_entry.get().strip()
        autor = self.autor_entry.get().strip()
        ano = self.ano_entry.get().strip()

        if not isbn or not titulo:
            messagebox.showerror("Erro", "ISBN e Título são obrigatórios!")
            return

        dados = {"titulo": titulo, "autor": autor, "ano": ano}
        self.arvore.insert(isbn, dados)

        messagebox.showinfo("OK", "Livro adicionado com sucesso!")
        self.window.destroy()

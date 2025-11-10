import tkinter as tk
from tkinter import ttk


class JanelaArvore:
    """Visualização da árvore com suporte a zoom e arrastar (pan).

    - Arrastar: botão esquerdo + mover (panning usando canvas.scan_*).
    - Zoom: roda do mouse (Windows: <MouseWheel>, Linux: Button-4/Button-5 também suportados).
    - Duplo clique: resetar e redesenhar na escala 1.0.
    """

    def __init__(self, root, arvore):
        self.root = root
        self.arvore = arvore

        self.window = tk.Toplevel(root)
        self.window.title("Visualização da Árvore Rubro-Negra")
        self.window.geometry("1000x650")

        frame = ttk.Frame(self.window)
        frame.pack(fill='both', expand=True)

        # canvas com barras de rolagem
        self.canvas = tk.Canvas(frame, width=980, height=600, bg="white")
        hbar = ttk.Scrollbar(frame, orient='horizontal', command=self.canvas.xview)
        vbar = ttk.Scrollbar(frame, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        self.canvas.grid(row=0, column=0, sticky='nsew')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='ew')

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # estado de interação
        self.scale = 1.0

        # Bindings: pan e zoom
        self.canvas.bind('<ButtonPress-1>', self._scan_start)
        self.canvas.bind('<B1-Motion>', self._scan_move)
        self.canvas.bind('<MouseWheel>', self._on_mousewheel)      # Windows / Mac
        self.canvas.bind('<Button-4>', self._on_mousewheel)        # Linux scroll up
        self.canvas.bind('<Button-5>', self._on_mousewheel)        # Linux scroll down
        self.canvas.bind('<Double-Button-1>', lambda e: self._reset_and_redraw())

        instr = ttk.Label(self.window, text="Arraste: botão esquerdo. Zoom: roda do mouse. Duplo clique para resetar.")
        instr.pack(side='bottom', pady=4)

        # desenha a árvore pela primeira vez
        self._desenhar_wrapper()

    def _desenhar_wrapper(self):
        self.canvas.delete("all")
        start_x = 500
        start_y = 40
        dx = 220
        self._desenhar(self.arvore.root, start_x, start_y, dx)
        self.canvas.update_idletasks()
        bbox = self.canvas.bbox("all")
        if bbox:
            self.canvas.config(scrollregion=bbox)

    def _desenhar(self, node, x, y, dx):
        if node is None or node.key is None:
            return

        r = 22  # raio do nó
        fill = "#D9534F" if getattr(node, 'color', None) == "RED" else "#222222"
        text_color = "white"

        # desenha linhas para filhos primeiro (para ficarem abaixo)
        if getattr(node, 'left', None) and getattr(node.left, 'key', None) is not None:
            self.canvas.create_line(x, y+r, x-dx, y+80-r, fill="#666666", width=2)
            self._desenhar(node.left, x-dx, y+80, dx//2)

        if getattr(node, 'right', None) and getattr(node.right, 'key', None) is not None:
            self.canvas.create_line(x, y+r, x+dx, y+80-r, fill="#666666", width=2)
            self._desenhar(node.right, x+dx, y+80, dx//2)

        # desenha nó sobre as linhas
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=fill, outline="#000000", width=1.5)
        display_key = str(node.key)
        self.canvas.create_text(x, y, text=display_key, fill=text_color, font=("Segoe UI", 9, "bold"))

    # ------------------ interação: pan e zoom ------------------
    def _scan_start(self, event):
        # marca posição para scan (pan)
        self.canvas.scan_mark(event.x, event.y)

    def _scan_move(self, event):
        # arrasta canvas
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def _on_mousewheel(self, event):
        # Determina fator (zoom in/out). Usa event.delta quando disponível (Windows).
        if hasattr(event, 'delta'):
            if event.delta > 0:
                factor = 1.1
            else:
                factor = 0.9
        else:
            # Para bindings Button-4 / Button-5 em Linux
            if getattr(event, 'num', None) == 4:
                factor = 1.1
            else:
                factor = 0.9

        # escala em torno do ponto do cursor (convertendo coords do widget para coords do canvas)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        try:
            self.canvas.scale('all', x, y, factor, factor)
        except Exception:
            return

        # atualizar fator acumulado e scrollregion
        self.scale *= factor
        self.canvas.update_idletasks()
        bbox = self.canvas.bbox('all')
        if bbox:
            self.canvas.config(scrollregion=bbox)

    def _reset_and_redraw(self):
        # redesenha na escala original (recria tudo)
        self.scale = 1.0
        self._desenhar_wrapper()
        

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os



class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #main window settings
        self.option_add("*tearOff", tk.FALSE)
        self.title("controle de estoque v 0.1")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))
        #creates menu
        menubar = tk.Menu(self)
        menu_informar = tk.Menu(self)
        menubar.add_cascade(menu= menu_informar,label= "Informar")
        menu_informar.add_command(label="Entrada de produto", command=lambda: InformarEntradaProduto())
        menu_informar.add_command(label="Saida de produto", command=lambda: InformarSaidaProduto())
        menu_informar.add_command(label="Contagem de produto", command=lambda: InformarContagemProduto())
        menu_consultar = tk.Menu(menubar)
        menubar.add_cascade(menu= menu_consultar,label= "Consultar")
        menu_consultar.add_command(label="Ficha de estoque de um produto", command=lambda: ConsultarFichaEstoque())
        menu_cadastrar = tk.Menu(menubar)
        menubar.add_cascade(menu= menu_cadastrar,label= "Cadastrar")
        menu_cadastrar.add_command(label="Produto", command=lambda: CadastrarProduto())
        menu_cadastrar.add_command(label="Grupo de produto", command=lambda: CadastrarGrupoProduto())
        self['menu'] = menubar
        label = tk.Label(self, text = "hello world").pack()

class InformarEntradaProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Informar entrada de produtos")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))
               

class InformarSaidaProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Informar saida de produtos")        
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))

class InformarContagemProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Informar contagem de produtos")        
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))

class ConsultarFichaEstoque(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Consultar ficha de estoque")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))

class CadastrarProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastrar um prouduto")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))

class CadastrarGrupoProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastrar um grupo de produtos")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))



if __name__ == "__main__":
    window = Window()
    window.mainloop()

import os
import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import string

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #main window settings
        self.option_add("*tearOff", tk.FALSE)
        self.title("controle de estoque v 0.1")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("images/inventory.png")))
        self.geometry("1200x500+0+0")
        #creates menu
        menubar = tk.Menu(self)
        menu_informar = tk.Menu(self)
        menubar.add_cascade(menu= menu_informar,label= "Informar")
        menu_informar.add_command(label="Entrada de produto", command= self.inform_inventory_input)
        menu_informar.add_command(label="Saida de produto", command= self.inform_inventory_withdraw)
        menu_informar.add_command(label="Contagem de produto", command= self.inform_inventory_count)
        menu_consultar = tk.Menu(menubar)
        menubar.add_cascade(menu= menu_consultar,label= "Consultar")
        menu_consultar.add_command(label="Ficha de estoque de um produto", command= self.check_inventory_record)
        menu_cadastrar = tk.Menu(menubar)
        menubar.add_cascade(menu= menu_cadastrar,label= "Gerenciar")
        menu_cadastrar.add_command(label="Cadastro de produtos", command= self.manage_products)
        menu_cadastrar.add_command(label="Grupos de produtos", command= self.manage_product_groups)
        self['menu'] = menubar
        tk.Label(self, text = "Aplicativo controle de estoque").pack()
        tk.Label(self, text = "v 0.1").pack()
        tk.Label(self, text = "Por Ederson Dias").pack()
        tk.Label(self, text = "").pack()
    
    def check_inventory_record(self):
        from check import inventory_record
        inventory_record.InventoryRecord()


    def inform_inventory_input(self):
        from inform import inventory_input
        inventory_input.IventoryInput()

    def inform_inventory_withdraw(self):
        from inform import inventory_withdraw
        inventory_withdraw.InventoryWithdraw()

    def inform_inventory_count(self):
        from inform import inventory_count
        inventory_count.InventoryCount()

    def manage_products(self):
        from manage import products
        products.manageProducts()

    def manage_product_groups(self):
        from manage import product_groups
        product_groups.manageProductsGroups()


if __name__ == "__main__":
    import create_db
    create_db.check_db()
    window = Window()
    window.mainloop()

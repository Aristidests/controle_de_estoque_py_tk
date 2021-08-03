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
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))
        self.geometry("400x300")
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
        tk.Label(self, text = "Aplicativo controle de estoque").pack()
        tk.Label(self, text = "v 0.1").pack()
        tk.Label(self, text = "Por Ederson Dias").pack()
        tk.Label(self, text = "").pack()
    
        
class CadastrarGrupoProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastrar um grupo de produtos")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))
        self.geometry("400x300")
        self.grid_rows = 0
        self.group_names_entry = [{}]
        tk.Label(self, text="Nome do grupo:").grid(row=str(self.grid_rows), column="0")
        self.grid_rows += 1
        self.new_group = tk.Button(self, text="+", command=self.add_entry).grid(row = str(self.grid_rows), column ="1", rowspan="2")
        self.save = tk.Button(self, text="Salvar", command=self.save_groups).grid(row = str(self.grid_rows), column ="2", rowspan="2")
        self.group_names_entry[0]['entry'] = tk.Entry(self, textvariable="")
        self.group_names_entry[0]['entry'].grid(row=str(self.grid_rows), column="0")
        self.grid_rows += 1


    def add_entry(self):
        self.group_names_entry.append({})
        newentry_num = len(self.group_names_entry)-1
        self.group_names_entry[newentry_num]['entry'] = tk.Entry(self, textvariable="")
        self.group_names_entry[newentry_num]['entry'].grid(row=str(self.grid_rows), column="0")
        self.grid_rows += 1
    
    def save_groups(self):
        dbconn = sqlite3.connect("db.sqlite3")
        dbcursor = dbconn.cursor()
        for entry_box in self.group_names_entry:
            for entry_box_value in entry_box.values():
                query_string = """
                INSERT INTO produtos_grupos (GRUPO)
                    VALUES ('""" + entry_box_value.get() + "');"
                dbcursor.execute(query_string)
        dbconn.commit()
        dbconn.close()

class CadastrarProduto(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastrar um prouduto")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("inventory.png")))
        tk.Label(self, text="Nome:").grid(row="0", column="0", padx="0")
        tk.Label(self, text="Marca:").grid(row="0", column="1")
        tk.Label(self, text="Grupo:").grid(row="0", column="2")
        tk.Label(self, text="Unidade:").grid(row="0", column="3")
        tk.Label(self, text="Codigo de Barra:").grid(row="0", column="4")
        self.entr_produto_nome = tk.Entry(self)
        self.entr_produto_nome.grid(row="1", column="0")
        self.entr_produto_marca = tk.Entry(self)
        self.entr_produto_marca.grid(row="1", column="1")
        self.cmbo_produto_grupo = ttk.Combobox(self, values = self.listar_grupos_de_produtos())
        self.cmbo_produto_grupo.grid(row="1", column="2")
        self.entr_produto_unidade = tk.Entry(self)
        self.entr_produto_unidade.grid(row="1", column="3")
        self.entr_produto_cod_barra = tk.Entry(self)
        self.entr_produto_cod_barra.grid(row="1", column="4")
        self.btn_salvar = tk.Button(self, text="Salvar Produto", command= self.salvar_produto)
        self.btn_salvar.grid(row="3", column="1", columnspan="2")
        ttk.Separator(self, orient="horizontal").grid(row="4", column="0")


    def listar_grupos_de_produtos(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        query = cursor.execute("SELECT * FROM produtos_grupos")
        query_result = query.fetchall()
        connection.close()
        l = []
        for grupo in query_result:
            l.append(grupo[0])
        return l

    def salvar_produto(self):
        produto = {
            "Nome": self.entr_produto_nome.get(),
            "Marca" : self.entr_produto_marca.get(),
            "Grupo" : self.cmbo_produto_grupo.get(),
            "Unidade" : self.entr_produto_unidade.get(),
            "Codbarra" : self.entr_produto_cod_barra.get()
            }
        
        def random_codbar():
            produto["Codbarra"] = "".join(random.choices(k= 13, population= string.digits))
        
        if produto["Codbarra"] == "":
            random_codbar()

        def check_duplicates():
            dbcon = sqlite3.connect("db.sqlite3")
            dbcursor = dbcon.cursor()
            dbcursor.execute("SELECT nome, marca FROM produtos WHERE nome = :Nome AND marca = :Marca", produto)
            duplicates = dbcursor.fetchall()
            dbcon.close()
            if len(duplicates) == 0:
                return False
            else: return True
        
        is_product_duplicate = check_duplicates()
        
        if is_product_duplicate == False:
            sql_query = str(
            """
            INSERT INTO produtos (nome,grupo,marca,unidade,codbar)
            VALUES(:Nome, :Grupo, :Marca, :Unidade, :Codbarra)
            """)
            dbcon = sqlite3.connect("db.sqlite3")
            dbcursor = dbcon.cursor()
            dbcursor.execute(sql_query, produto)
            dbcon.commit()
            dbcon.close()
        else: print("Produto Duplicado")
         



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





if __name__ == "__main__":
    import create_db
    create_db.check_db()
    window = Window()
    window.mainloop()

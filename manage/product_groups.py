import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import pandas as pd
from images import app_icons

icons = {
    "add" : app_icons.add(25,25),
    "rm" : app_icons.remove(25,25),
    "edit": app_icons.edit(25,25),
    "ok": app_icons.ok(25,25)
}

class manageProductsGroups(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Gerenciar grupos de produtos")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("images/inventory.png")))
        self.geometry("600x400+0+0")
        self.resizable(False, False)
        self.lf_1 = ttk.Labelframe(self, text="Incluir novo grupo de produtos:")
        self.lf_1.place(relx = 0.01, relwidth= 0.99, y = 1, height= 100)
        self.entry_new_group_name = tk.Entry(self.lf_1)
        self.entry_new_group_name.place(in_= self.lf_1, relx = 0.01, relwidth= 2/3, rely= 0.1, relheight= 0.5)
        self.btn_add_new_group = tk.Button(self.lf_1, text= "Incluir", image = icons["add"], compound= tk.LEFT, command = self.save_new_group)
        self.btn_add_new_group.place(in_= self.lf_1, relx = (2/3)+0.01, relwidth= (1/3)-0.01, rely= 0, relheight= 0.7)
        self.lf_2 = ttk.Labelframe(self, text= "Grupos disponíveis", padding= "5px")
        self.lf_2.place(relx = 0.01, relwidth= 0.99, y = 110, height= 280)
        self.create_lb_avaiable_groups()
        self.btn_edit_group = ttk.Button(self.lf_2, text="Editar", image= icons["edit"], compound= tk.LEFT, command= self.edit_group)
        self.btn_edit_group.place(in_= self.lf_2, relx = 0.76, relwidth= 0.22, rely= 0, relheight= 0.2)
        self.btn_rm_group = ttk.Button(self.lf_2, text="Remover", image= icons["rm"], compound= tk.LEFT, command= self.remove_group)
        self.btn_rm_group.place(in_= self.lf_2, relx = 0.76, relwidth= 0.22, rely= 0.21, relheight= 0.2)
    
    def create_lb_avaiable_groups(self):
        """Creates tk listbox widget containing avaiable groups"""
        if  hasattr(manageProductsGroups, "lb_avaiable_groups"):
             self.lb_avaiable_groups.destroy()
        self.get_avaiable_groups()
        self.lb_avaiable_groups = tk.Listbox(self.lf_2, activestyle= "dotbox", listvariable= tk.StringVar(value = self.df_product_groups["product_group"].tolist()))
        self.lb_avaiable_groups.place(in_= self.lf_2, relx = 0, relwidth= 0.75, rely= 0, relheight= 0.9)
        self.lb_avaiable_groups.bind("<<ListboxSelect>>", self.set_selected_group)

    def edit_group(self):
        print("Editing group: " + str(self.selected_group))
        self.geometry("600x480")
        self.lf_3 = ttk.Labelframe(self, text="Novo nome do grupo: " + self.selected_group["name"])
        self.lf_3.place(relx= 0.01, relwidth= 0.99, y = 400, height= 100)
        self.entry_chgd_group_name = tk.Entry(self.lf_3)
        self.entry_chgd_group_name.place(relx= 0.01, relwidth=2/3, y = 0, height= 50)
        self.btn_update_group = tk.Button(self.lf_3, text= "Confirmar", image= icons["ok"], compound= tk.LEFT, command= self.update_group)
        self.btn_update_group.place(relx= (2/3)+0.01, relwidth= (1/3)-0.01, y= 0, height=50)

    def get_avaiable_groups(self):
        """Returns dataframe object containing products groups"""
        dbcon = sqlite3.connect("db.sqlite3")
        self.df_product_groups = pd.read_sql_query("SELECT * FROM products_groups", dbcon)
        print(self.df_product_groups)
        dbcon.close()

    def remove_group(self):
        selected_group = {"group": self.selected_group}
        print("Removing group: " + selected_group["group"])
        dbcon = sqlite3.connect("db.sqlite3")
        dbcrsr = dbcon.cursor()
        dbquery = "DELETE FROM products_groups WHERE product_group = :group;"
        dbcrsr.execute(dbquery, selected_group)
        dbcon.commit()
        dbcon.close()
        self.create_lb_avaiable_groups()

    def set_selected_group(self, event):
        """Callback function which resturns selected group from the listbox"""
        selection = self.lb_avaiable_groups.curselection()
        print(selection)
        if selection == ():
            return
        selection = self.lb_avaiable_groups.get(selection)
        self.selected_group = {
            "id" : self.df_product_groups[self.df_product_groups["product_group"] == selection]["id"].iloc[0],
            "name": selection
        }

    def save_new_group(self):
        if self.entry_new_group_name.get() == "":
            print("No group to add")
            return
        group = {"group" : self.entry_new_group_name.get()}
        print(group)
        print(group["group"])
        dbcon = sqlite3.connect("db.sqlite3")
        dbcrsr = dbcon.cursor()
        dbcrsr.execute("""
        INSERT INTO products_groups (product_group)
        VALUES (:group)
        """,
        group)
        dbcon.commit()
        dbcon.close()
        self.entry_new_group_name.delete(0, tk.END)
        self.create_lb_avaiable_groups()
        print("Group " + group["group"] + " added")
    
    def update_group(self):
        chgd_group_name = self.entry_chgd_group_name.get()
        if chgd_group_name == "":
            print("No change to do")
            return
        print(chgd_group_name)
        chgd_group_name = {
            "id" : str(self.selected_group["id"]),
            "name" : chgd_group_name
        }
        print(chgd_group_name)
        dbconn = sqlite3.connect("db.sqlite3")
        dbcrsr = dbconn.cursor()
        sql_query = (
            """
            UPDATE products_groups
            SET product_group = :name
            WHERE id = :id;
            """
        )
        dbcrsr.execute(sql_query, chgd_group_name)
        dbconn.commit()
        dbconn.close()
        print(type(chgd_group_name["id"]))
        print("Group " + self.selected_group["name"] + " CHanged to: " + chgd_group_name["name"])
        self.lf_3.destroy()
        self.geometry("600x400")
        self.create_lb_avaiable_groups()

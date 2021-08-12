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

class InventoryCount(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Informar contagem de produtos (Balanço)")
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open("images/inventory.png")))
        self.geometry("600x400+0+0")
        self.resizable(False, False)
        tk.Label(self, text= "In developement").pack()
        
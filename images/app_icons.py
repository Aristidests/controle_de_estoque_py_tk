import tkinter as tk
from PIL import Image, ImageTk


def add(width = None, heigth = None):
    image = Image.open("images/add_icon.png")
    if width == None and heigth == None:
        return ImageTk.PhotoImage(image)
    if width == None:
        width = image.width
    if heigth == None:
        image = image.height
    image = image.resize((width, heigth), Image.ANTIALIAS)
    return  ImageTk.PhotoImage(image)

def remove(width = None, heigth = None):
    image = Image.open("images/remove_icon.png")
    if width == None and heigth == None:
        return ImageTk.PhotoImage(image)
    if width == None:
        width = image.width
    if heigth == None:
        image = image.height
    image = image.resize((width, heigth), Image.ANTIALIAS)
    return  ImageTk.PhotoImage(image)

def edit(width = None, heigth = None):
    image = Image.open("images/edit_icon.png")
    if width == None and heigth == None:
        return ImageTk.PhotoImage(image)
    if width == None:
        width = image.width
    if heigth == None:
        image = image.height
    image = image.resize((width, heigth), Image.ANTIALIAS)
    return  ImageTk.PhotoImage(image)

def ok(width = None, heigth = None):
    image = Image.open("images/ok_icon.png")
    if width == None and heigth == None:
        return ImageTk.PhotoImage(image)
    if width == None:
        width = image.width
    if heigth == None:
        image = image.height
    image = image.resize((width, heigth), Image.ANTIALIAS)
    return  ImageTk.PhotoImage(image)
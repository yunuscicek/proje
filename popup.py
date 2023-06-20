from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import keyboard

# keyboard.wait("h")

root = tkinter.Tk()


def quit_program(e):
    root.destroy()


# def open_win():
#     new = Toplevel(root)
#     new.geometry("250x300")
#     new.title("ceviri popupu")
#     Label(new, text="ceviriler buraya gelecek").pack(pady=30)


Label(text="ceviriler buraya gelecek").pack(pady=20)

# root.bind("<Alt-z>", open_win)

root.bind("<FocusOut>", quit_program)

root.mainloop()

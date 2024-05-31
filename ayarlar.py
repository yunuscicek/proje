import pyautogui as pyag
from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import ayarlarKaydet as ak

def AyarlarPencere():
        
    def degerKaydet():
            
        boyut = e1.get()
        font  = e2.get()
        bind = e3.get()
        ak.KaydetFonk(boyut, font, bind)

    def on_validate(P):

        if P.isdigit():

                return True
        
        else:
                return False
           
    pencere = Tk()
    pencere.title(" ")
    pencere.geometry("100x150")
    pencere.resizable(False,False)
    pencere.iconbitmap("./icons/settings.png")
    pencere.eval("tk::PlaceWindow . center")
    pencere.attributes("-topmost", not pencere.attributes("-topmost"))

    with open("config.json", "r") as ff:
            
            data = json.load(ff)  
    
    for config in data["config"]:
            
            font_size = config["size"]   
            font_type = config["font"]  
            bind = config["bind"]  

    label1 = Label(pencere, text = "Boyut")
    label1.pack(anchor=NW,expand=TRUE)
    
    vcmd = pencere.register(on_validate)

    e1 = ttk.Combobox(pencere, validate="key", validatecommand =(vcmd, '%P'), values = [str(i) for i in range(5,31)])
    e1.pack(anchor = NW, expand = TRUE)
    e1.insert(0, font_size)
    e1.select_range(0, END)
   
    label2 = Label(pencere, text = "Font")
    label2.pack(anchor = NW, expand = TRUE)
   
    e2 = ttk.Combobox(pencere, values = ["Segoe UI", "Arial", "Verdana", "Times New Roman", "Courier New"])
    e2.pack(anchor = NW, expand = TRUE)
    e2.insert(0,font_type)

    label3 = Label(pencere, text = "Kısayol tuşu")
    label3.pack(anchor = NW, expand = TRUE)

    e3 = ttk.Combobox(pencere, values = ["alt-x", "alt-z","alt-s","alt-c"])
    e3.insert(0,bind)
    e3.pack(anchor = NW, expand = TRUE)
    
    def on_entry_click(event):
            
            e2.select_range(0, END) 
            return 'break'
    
    e1.bind('<FocusIn>', on_entry_click)

    button1 = Button(pencere, text = "Kaydet", command = degerKaydet)
    button1.pack(anchor = S, expand = TRUE)
           
    pencere.mainloop()
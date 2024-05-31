from tkinter import *
from tkinter import ttk
import json


def KaydetFonk(font_size,font_type,bind):

    with open("config.json", "r") as ff:

        data = json.load(ff)

    for config in data["config"]:

        config["size"] = font_size  
        config["font"] = font_type
        config["bind"] = bind
    
    with open ("config.json", "w") as ff:
        
        json.dump(data, ff)
        
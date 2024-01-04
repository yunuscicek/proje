import pyautogui as pyag
from tkinter import *
from tkinter import ttk
import threading
import googletranslate as gt
import CambridgeCeviri as cc
import LongmanCeviri as lc

class Pencere:

    def PencereOlustur(self, selected_text, kelimeSayisi):
        
        x,y = pyag.position()

        pencere = Tk()
        pencere.title("Çeviri")
        pencere.geometry(f"+{x}+{y}")
        sekmeKontrol = ttk.Notebook(pencere) 
        
        pencere.attributes('-topmost', not pencere.attributes('-topmost'))
        
        sekme1 = ttk.Frame(sekmeKontrol) 
        sekme2 = ttk.Frame(sekmeKontrol) 
        sekme3 = ttk.Frame(sekmeKontrol) 
  
        sekmeKontrol.add(sekme1, text ='Google Translate') 
        sekmeKontrol.add(sekme2, text ='Cambridge Dict.') 
        sekmeKontrol.add(sekme3, text ='Longman Dict.') 
        sekmeKontrol.pack(expand=1, fill="both")
        
        text = Text(pencere, width = 60, height = 20, font = ("Segoe UI",11))
        text.pack(padx=5, pady=5)
        text.config(state=DISABLED)

        gtranslated = StringVar()
        ctranslated = StringVar()
        ltranslated = StringVar()

        gtranslated.set("Loading...")
        ctranslated.set("Loading...")
        ltranslated.set("Loading...")
        
        def google(text):
            gtranslated.set(gt.Ceviri(text))
            update()
        def cbridge(text):
            ctranslated.set(cc.Ceviri(text))
            update()
        def lman(text):
            ltranslated.set(lc.Ceviri(text))
            update()

        threadgt = threading.Thread(target=google,args=(selected_text,))
        threadcc = threading.Thread(target=cbridge,args=(selected_text,))
        threadlc = threading.Thread(target=lman,args=(selected_text,))
        threadgt.start()
        threadcc.start()
        threadlc.start()

        def on_tab_change(event):
            update()

        def update():
            current_tab = sekmeKontrol.index(sekmeKontrol.select())
            
            if(current_tab == 0):
                
                text.config(state=NORMAL)
                text.delete("1.0", "end")
                text.insert(INSERT, gtranslated.get())
                text.config(state=DISABLED)

            elif(current_tab == 1):
                
                text.config(state=NORMAL)
                text.delete("1.0", "end")
                
                if(kelimeSayisi<=3):
                    text.insert(INSERT, ctranslated.get())
                    text.config(state=DISABLED)
                else:

                    return

            elif(current_tab == 2):
                
                text.config(state=NORMAL)
                text.delete("1.0", "end")
                
                if(kelimeSayisi<=3):
                    text.insert(INSERT, ltranslated.get())
                    text.config(state=DISABLED)
                else:

                    return

        sekmeKontrol.bind("<<NotebookTabChanged>>", on_tab_change)

        pencere.mainloop()
    

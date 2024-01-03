import pyautogui as pyag
from tkinter import *
from tkinter import ttk
import myNB as NB
import time

class Pencere:

    def PencereOlustur(self, metinGT, metinCC, metinLC, kelimeSayisi):
        
        zamanBaslangic = time.time()
        print("pencere baslangic")
        print(time.time() - zamanBaslangic)

        x,y = pyag.position()

        pencere = Tk()
        pencere.title("Çeviri")
        pencere.geometry(f"+{x}+{y}")
        sekmeKontrol = NB.myNotebook(pencere) 
  
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

        print("pencere fonksiyon: ")
        print(time.time() - zamanBaslangic)

        def on_tab_change(event):
            
            current_tab = sekmeKontrol.index(sekmeKontrol.select())
            
            if(current_tab == 0):

                text.config(state=NORMAL)
                text.delete("1.0", "end")
                text.insert(INSERT, metinGT)
                text.config(state=DISABLED)

            elif(current_tab == 1):

                text.config(state=NORMAL)
                text.delete("1.0", "end")
                
                if(kelimeSayisi<3):
                    text.insert(INSERT, metinCC)
                    text.config(state=DISABLED)
                else:

                    return

            elif(current_tab == 2):

                text.config(state=NORMAL)
                text.delete("1.0", "end")
                
                if(kelimeSayisi<3):
                    text.insert(INSERT, metinLC)
                    text.config(state=DISABLED)
                else:

                    return

        sekmeKontrol.bind("<<NotebookTabChanged>>", on_tab_change)

        pencere.mainloop()
    

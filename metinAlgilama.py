import keyboard
import pyperclip
import pyautogui as pya
import pencere as pk
import googletranslate as gt
import CambridgeCeviri as cc
import LongmanCeviri as lc
import time
import myNB as NB

keyboard.add_hotkey('alt+x', lambda: translate_clipboard())

p = pk.Pencere()

def translate_clipboard():

    zamanBaslangic = time.time()
    print("fonksiyona giriş: ")
    print(time.time() - zamanBaslangic)

    time.sleep(0.25)
    pya.hotkey('ctrl', 'c')
    
    selected_text = pyperclip.paste()
    selected_text = selected_text.lower()
    degistirme_karakteri = "-"
    bosluk_sayisi = sum(1 for char in selected_text if char.isspace())
    
    print(time.time()- zamanBaslangic)

    if(bosluk_sayisi == 0):
        
        p.PencereOlustur(gt.GoogleTranslateKelimeCeviri(selected_text),cc.CambridgeKelimeCeviri(selected_text),lc.LongmanKelimeCeviri(selected_text), (bosluk_sayisi + 1))
        
    elif(bosluk_sayisi == 1):
        
        selected_text_tire = selected_text.replace(" ", degistirme_karakteri)
        p.PencereOlustur(gt.GoogleTranslateKelimeCeviri(selected_text),cc.CambridgeKelimeCeviri(selected_text_tire),lc.LongmanKelimeCeviri(selected_text_tire), (bosluk_sayisi + 1))
        
    else:

        p.PencereOlustur(gt.GoogleTranslateCumleCeviri(selected_text), None, None, (bosluk_sayisi + 1))
    
keyboard.wait("esc")

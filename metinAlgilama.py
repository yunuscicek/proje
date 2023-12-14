import keyboard
import pyperclip
import pyautogui as pya
import pencere as pk
import googletranslate as gt
import CambridgeCeviri as cc
import LongmanCeviri as lc
import time

keyboard.add_hotkey('alt+x', lambda: translate_clipboard())
p = pk.Pencere()

def translate_clipboard():
    time.sleep(0.3)
    pya.hotkey('ctrl', 'c')
    selected_text = pyperclip.paste()
    
    bosluk_sayisi = sum(1 for char in selected_text if char.isspace())
    
    if(bosluk_sayisi == 0):
        p.PencereOlustur(gt.GoogleTranslateKelimeCeviri(selected_text),cc.CambridgeKelimeCeviri(selected_text),lc.LongmanKelimeCeviri(selected_text), (bosluk_sayisi + 1))
      
    elif(bosluk_sayisi == 1):
        p.PencereOlustur(gt.GoogleTranslateKelimeCeviri(selected_text),cc.CambridgeKelimeCeviri(selected_text),lc.LongmanKelimeCeviri(selected_text), (bosluk_sayisi + 1))
      
    else:
        p.PencereOlustur(gt.GoogleTranslateCumleCeviri(selected_text), None, None, (bosluk_sayisi + 1))
keyboard.wait("esc")

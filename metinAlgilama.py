import keyboard
import pyperclip
import pyautogui as pya
import pencere as pk
import googletranslate as gt
import CambridgeCeviri as cc
import LongmanCeviri as lc
import time

def on_key_release(e):
    if e.name == 'alt' and keyboard.is_pressed('x'):  # Check if Alt and X keys are released
        translate_clipboard()

keyboard.on_release_key('alt', on_key_release)

p = pk.Pencere()

def translate_clipboard():

    zamanBaslangic = time.time()
    print("fonksiyona giriş: ")
    print(time.time() - zamanBaslangic)

    pya.hotkey('ctrl', 'c')
    
    selected_text = pyperclip.paste()
    selected_text = selected_text.lower()
    degistirme_karakteri = "-"
    bosluk_sayisi = sum(1 for char in selected_text if char.isspace())
    
    print(time.time()- zamanBaslangic)
    p.PencereOlustur(selected_text, (bosluk_sayisi + 1))
    
keyboard.wait("esc")


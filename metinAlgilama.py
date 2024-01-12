import keyboard
import pyperclip
import pyautogui as pya
import pencere as pk

def on_key_release(e):
    if e.name == 'alt' and keyboard.is_pressed('x'):  # Check if Alt and X keys are released
        translate_clipboard()

keyboard.on_release_key('alt', on_key_release)

p = pk.Pencere()

def translate_clipboard():

    pya.hotkey('ctrl', 'c')
    
    selected_text = pyperclip.paste()
    selected_text = selected_text.lower()
    selected_text = selected_text.strip()
    bosluk_sayisi = sum(1 for char in selected_text if char.isspace())
    
    p.PencereOlustur(selected_text, (bosluk_sayisi + 1))
    
keyboard.wait("esc")

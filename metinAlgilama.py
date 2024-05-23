import keyboard
import pyperclip
import pyautogui as pya
import pencere as pk
import json

with open ("config.json","r") as ff:

    data = json.load(ff)

for config in data["config"]:
    
    bind = config["bind"]

parts = bind.split("-")
parts = [part.strip() for part in parts]
x1, x2 = parts
print(x1,x2)
def on_key_release(e):
    if e.name == x1 and keyboard.is_pressed(x2):
        translate_clipboard()

keyboard.on_release_key(x1, on_key_release)

p = pk.Pencere()

def translate_clipboard():

    pya.hotkey("ctrl", "c")
    
    selected_text = pyperclip.paste()
    selected_text = selected_text.lower()
    selected_text = selected_text.strip()
    bosluk_sayisi = sum(1 for char in selected_text if char.isspace())
    
    p.PencereOlustur(selected_text, (bosluk_sayisi + 1))
    
keyboard.wait("esc")

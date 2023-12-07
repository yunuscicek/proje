import keyboard
import pyperclip
import pyautogui as pya
import time

keyboard.add_hotkey('alt+x', lambda: translate_clipboard())

def translate_clipboard():
    time.sleep(1)
    pya.hotkey('ctrl', 'c')
    
    selected_text = pyperclip.paste()
    print(selected_text)
    

keyboard.wait("esc")

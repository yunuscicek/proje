import keyboard
import pyperclip
from googletrans import Translator
import pyautogui as pya
import time
translator = Translator()

keyboard.add_hotkey('alt+x', lambda: translate_clipboard())

def translate_clipboard():
    time.sleep(0.1)
    pya.hotkey('ctrl', 'c')
    
    selected_text = pyperclip.paste()
    print(selected_text)
    

keyboard.wait("esc")

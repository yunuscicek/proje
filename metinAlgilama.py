import keyboard
import pyperclip
from googletrans import Translator

translator = Translator()

keyboard.add_hotkey('alt+z', lambda: translate_clipboard())

def translate_clipboard():
 
    selected_text = pyperclip.paste()

    ceviri = translator.translate(selected_text, dest='tr')

  
    pyperclip.copy(ceviri.text)


    print(ceviri.text)

keyboard.wait('esc')
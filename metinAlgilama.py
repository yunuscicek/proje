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

# import pyperclip
# import pygetwindow as gw
# import keyboard

# # Function to capture text from the currently focused window and copy it to the clipboard
# def copy_selected_text_to_clipboard(e):
#     if e.event_type == keyboard.KEY_DOWN and e.name == 'alt+x':
#         window = gw.getWindowsWithTitle('Your Window Title')[0]  # Replace with your window title
#         selected_text = window.get_clipboard()
#         pyperclip.copy(selected_text)

# # Monitor for Alt+X keypress events
# keyboard.hook(copy_selected_text_to_clipboard)

# # Keep the script running
# keyboard.wait()

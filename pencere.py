import pyautogui as pyag
import time
import tkinter as tk

time.sleep(1)
# print(pyag.size())   # resolution
print(pyag.position()) # cursor position by x,y

x,y = pyag.position()
pencere = tk.Tk()
pencere.title("as")
pencere.geometry(f"+{x}+{y}")
tk.mainloop()
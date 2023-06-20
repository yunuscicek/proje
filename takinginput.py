# import tkinter as tk

# def on_selection(event):
#     selected_text = event.widget.selection_get()
    
#     print("Selected Text:", selected_text)

# def on_key_press(event):
    
#     if (
#         event.state == 4 and event.keysym.lower() == "s"
#     ): 
#         widget = event.widget
#         selected_text = widget.selection_get()
       
#         print("Selected Text:", selected_text)

# root = tk.Tk()

# text_widget = tk.Text(root)
# text_widget.pack()

# text_widget.bind("<ButtonRelease-1>", on_selection)

# root.bind("<KeyPress>", on_key_press)

# root.mainloop()

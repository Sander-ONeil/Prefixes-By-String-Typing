import tkinter as tk

from prefix_experiments import *

def on_key(event):
    label.config(text=entry.get())
    terms = break_into_terms(entry.get())
    terms_values = convert(terms)

    for x in terms_values:
        x.show()
    
    
    RESULT = mult(terms_values)
        
    RESULT.show_in_terms()

root = tk.Tk()
root.title('Live Text Display')

entry = tk.Entry(root)
entry.pack(pady=20, padx=20)
entry.bind('<KeyRelease>', on_key)

label = tk.Label(root, text='')
label.pack(pady=20, padx=20)

root.mainloop()

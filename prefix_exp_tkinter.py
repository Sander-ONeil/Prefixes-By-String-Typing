#!/usr/bin/python3

import tkinter as tk

from prefix_experiments import *

def on_key(event):
    #label.config(text=entry.get())
    terms = break_into_terms(entry.get())
    terms_values = convert(terms)
    
    RESULT = mult(terms_values)
        
    ans = RESULT.show_in_terms()
    
    label.config(text=ans)
    
    ans_imp = RESULT.show_in_terms_imp()
    
    imperial_label.config(text = ans_imp)
    

def insert_character(char):
    entry.insert(tk.END, char)  # Insert the character at the end of the entry
    on_key(None)  # Update the result

root = tk.Tk()
root.title('Live Text Display')

entry = tk.Entry(root,font=("Arial", 20),width=52)
entry.grid(row=0, column=0, pady=20, padx=20, sticky="ew",) # Grid placement for entry
entry.bind('<KeyRelease>', on_key)

label = tk.Label(root, text='metric', font=("Arial", 20)) # Font adjusted to make text bigger
label.grid(row=1, column=0, pady=20, padx=20, sticky="ew")
imperial_label = tk.Label(root, text='imperial', font=("Arial", 20)) # Font adjusted to make text bigger
imperial_label.grid(row=2, column=0, pady=20, padx=20, sticky="ew")




button_text = ['×','÷','°','μ','π','Ω','c (speed of light)','Density of Water','g_earth','molarity','G (gravitational constant)','ε_0']




for i, t in enumerate(button_text):
    
    tk.Button(root, text=t, command=lambda t=t: insert_character(t)).grid(row=i%3, column=1+i//3, pady=5, padx=5)
  # Grid

# Ensure column 0 takes all extra space
root.grid_columnconfigure(0, weight=1)


root.mainloop()



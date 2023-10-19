import tkinter as tk

from prefix_experiments import *

def on_key(event):
    #label.config(text=entry.get())
    terms = break_into_terms(entry.get())
    terms_values = convert(terms)
    
    RESULT = mult(terms_values)
        
    ans = RESULT.show_in_terms()
    
    
    metric_label.configure(state="normal")
    metric_label.delete(1.0, tk.END)
    #imperial_label.config(text = ans_imp)
    metric_label.insert(1.0,ans,'center')
    metric_label.configure(state="disabled")
    
    
    ans_imp = RESULT.show_in_terms_imp()
    
    imperial_label.configure(state="normal")
    imperial_label.delete(1.0, tk.END)
    #imperial_label.config(text = ans_imp)
    imperial_label.insert(1.0,ans_imp,'center')
    imperial_label.configure(state="disabled")
    
    ans_con = RESULT.show_in_terms_con()
    con.configure(state="normal")
    con.delete(1.0, tk.END)
    #imperial_label.config(text = ans_imp)
    con.insert(1.0,ans_con,'center')
    con.configure(state="disabled")
    

def insert_character(char):
    entry.insert("insert", char)  # Insert the character at the end of the entry
    on_key(None)  # Update the result


help_string = "Use \"[ term ] ^ x\" for exponents like squaring or square roots and  \"val prefix unit ^ x\" for exponential units"

m = 7
root = tk.Tk()
root.title('Live Text Display')

entry = tk.Entry(root,font=("Arial", 20),width=62)
entry.grid(row=m+0, column=0, pady=20, padx=20, sticky="ew",columnspan = 5) # Grid placement for entry
entry.bind('<KeyRelease>', on_key)

def clear_text():
   entry.delete(0, tk.END)
   on_key(None)


tk.Button(root,text = 'CLEAR',command=clear_text,font=("Arial", 20)).grid(row=m+0,column=6)

# label = tk.Label(root, text='metric', font=("Arial", 20)) # Font adjusted to make text bigger
# label.grid(row=m+1, column=0, pady=20, padx=20, sticky="ew",columnspan = 5)




metric_label = tk.Text(root,height=1,width = 1, font=("Arial", 20)) # Font adjusted to make text bigger

metric_label.tag_configure('center', justify='center')
metric_label.insert(1.0,'Metric','center')

metric_label.grid(row=m+2, column=0, pady=20, padx=10, sticky="ew",columnspan = 5)

metric_label.configure(state="disabled")
metric_label.configure(bg=root.cget('bg'), relief="flat")




imperial_label = tk.Text(root,height=1,width = 1, font=("Arial", 20)) # Font adjusted to make text bigger

imperial_label.tag_configure('center', justify='center')
imperial_label.insert(1.0,'Imperial','center')

imperial_label.grid(row=m+3, column=0, pady=20, padx=20, sticky = "ew" ,columnspan = 5)

imperial_label.configure(state="disabled")
imperial_label.configure(bg=root.cget('bg'), relief="flat")



con = tk.Text(root,height=1,width = 1, font=("Arial", 15)) # Font adjusted to make text bigger

con.tag_configure('center', justify='center')
con.insert(1.0,'Base units','center')

con.grid(row=m+1, column=0, pady=20, padx=20, sticky = "ew" ,columnspan = 5)

con.configure(state="disabled")
con.configure(bg=root.cget('bg'), relief="flat")





# w = tk.Text(root, height=1)
# w.grid(row=m+1, column=0, pady=20, padx=20, sticky="ew",columnspan = 5)


# w.configure(bg=root.cget('bg'), relief="flat")



# w.insert(1.0, 'Metric')
# w.configure(state="disabled")

button_text = ['×','÷','°','μ','π','Ω','Å','ε_0','k_e','H_0','c_speed of light','Density of Water','g_earth','molarity','G_gravitational constant','Planck_length',
    'Planck_mass',
    'Planck_time',
    'Planck_temperature',
    'earth_circumference',
    'Age_of_universe',
    'mass_sun',
    'mass_earth',
    'mass_moon',
    'R_earth',

]




for i, t in enumerate(button_text):
    
    tk.Button(root, text=t, command=lambda t=t: insert_character(t)).grid(row=i%m, column=0+i//m, pady=5, padx=5)
  # Grid

# Ensure column 0 takes all extra space
#root.grid_columnconfigure(0, weight=1)


root.mainloop()



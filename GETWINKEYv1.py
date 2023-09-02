
import tkinter as tk
from tkinter import messagebox
import random

def on_option_change(event):
    selected_option = dropdown_var.get()

def exit_application():
    root.destroy()

def generate_key():
    selected_option = dropdown_var.get()
    
    key_mappings = {
        "WINXP": [
            "DB8YF-HTGKP-6C948-3BHYD-PH2PB",
            "B66VY-4D94T-TPPD4-43F72-8x4FY",
            "DTWB2-VX8WY-FG8R3-X696T-66Y46",
            "DTWB2-VX8WY-FG8R3-X696T-66Y46",
            "VCFQD-V9FX9-46WVH-K3CD4-4J3JM"
        ],
        "WIN7PRO": [],
        "WIN7ULT": []  
    }
    
    if selected_option in key_mappings:
        keys = key_mappings[selected_option]
        if keys:
            prev_key = key_label["text"]
            new_key = prev_key
            while new_key == prev_key:
                new_key = random.choice(keys)
            key_label.config(text=new_key)
        else:
            key_label.config(text="No keys available for this option.")
    else:
        key_label.config(text="Invalid option selected.")


def open_about_popup():
    about_text = "GETWINKEY v1\n\nGETWINKEY v1\n\nAuthor: Txmm"
    messagebox.showinfo("About", about_text)

root = tk.Tk()
root.geometry("400x400") 

label = tk.Label(root, text="GETWINKEY v1", font=("Helvetica", 14))
label.pack(pady=10)

options = ["WINXP", "WIN7PRO", "WIN7ULT"]

dropdown_var = tk.StringVar(root)
dropdown_var.set(options[0])  

dropdown_menu = tk.OptionMenu(root, dropdown_var, *options, command=on_option_change)
dropdown_menu.pack(side=tk.BOTTOM, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, padx=10, pady=10)

about_button = tk.Button(button_frame, text="About", command=open_about_popup)
about_button.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(button_frame, text="Generate", command=generate_key)
generate_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_application)
exit_button.pack(side=tk.RIGHT, padx=5)

key_label = tk.Label(root, text="", font=("Helvetica", 12))
key_label.pack(pady=10)

root.mainloop()

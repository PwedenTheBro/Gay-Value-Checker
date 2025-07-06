import tkinter as tk
from tkinter import messagebox

# The Gay Function
def check_value():
    try:
        value = int(entry.get())
        if value == 69:
            result_label.config(text="🌈 Value is gay!", fg="hot pink")
        else:
            result_label.config(text="Value is not gay.", fg="gray")
    except ValueError:
        messagebox.showerror("Wrong") ("were trying to figure out if You're gay not an idiot")

def reset_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Main window
root = tk.Tk()
root.title("Value Checker")
root.geometry("1920x1080")
root.configure(bg="#1e1e2f")  # Mörk bakgrund

# Headline
title = tk.Label(root, text="Is your value gay?", font=("Arial", 70, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=20)

# Inmatningsfält
entry = tk.Entry(root, font=("Arial", 70))
entry.pack(pady=10)

# Check-button
check_button = tk.Button(root, text="Check Value", command=check_value, font=("Arial", 30), bg="lightblue")
check_button.pack(pady=10)

# Reset-button
reset_button = tk.Button(root, text= "RESET", command=reset_fields, font=("Arial", 20), bg="orange")
reset_button.pack(pady=10)


# Result-text
result_label = tk.Label(root, text="", font=("Arial", 70), bg="#1e1e2f")
result_label.pack(pady=20)

# Start GUI
root.mainloop()
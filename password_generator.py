import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Invalid Length", "Password length must be at least 1.")
            return

        # Character set based on user selection
        characters = ""
        if use_uppercase.get():
            characters += string.ascii_uppercase
        if use_lowercase.get():
            characters += string.ascii_lowercase
        if use_numbers.get():
            characters += string.digits
        if use_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Invalid Selection", "Please select at least one character type.")
            return

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        password_entry.config(state=tk.NORMAL)  # Enable editing temporarily
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")  # Set back to read-only

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Function to clear password
def clear_password():
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#fafafa")  # Light background

# Header
header_frame = tk.Frame(root, bg="#4169E1", height=80)  # Royal blue header
header_frame.pack(fill="x")
title_label = tk.Label(header_frame, text="Password Generator", font=("Arial", 18, "bold"), fg="white", bg="#4169E1")
title_label.place(relx=0.5, rely=0.5, anchor="center")

# Options Frame
options_frame = tk.Frame(root, bg="#fafafa")
options_frame.pack(pady=15)

length_label = tk.Label(options_frame, text="Password Length:", font=("Arial", 12), bg="#fafafa", fg="#333333")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

length_entry = tk.Entry(options_frame, font=("Arial", 12), width=5, bg="#ffffff", relief="solid", borderwidth=1)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Checkbuttons for character type selection
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

uppercase_check = tk.Checkbutton(options_frame, text="Include Uppercase", variable=use_uppercase, font=("Arial", 10), bg="#fafafa", fg="#333333", selectcolor="#e3e3e3")
uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

lowercase_check = tk.Checkbutton(options_frame, text="Include Lowercase", variable=use_lowercase, font=("Arial", 10), bg="#fafafa", fg="#333333", selectcolor="#e3e3e3")
lowercase_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

numbers_check = tk.Checkbutton(options_frame, text="Include Numbers", variable=use_numbers, font=("Arial", 10), bg="#fafafa", fg="#333333", selectcolor="#e3e3e3")
numbers_check.grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

special_check = tk.Checkbutton(options_frame, text="Include Special Characters", variable=use_special, font=("Arial", 10), bg="#fafafa", fg="#333333", selectcolor="#e3e3e3")
special_check.grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

# Password Entry Frame
password_frame = tk.Frame(root, bg="#fafafa")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Generated Password:", font=("Arial", 12), bg="#fafafa", fg="#333333")
password_label.grid(row=0, column=0, padx=10)

password_entry = tk.Entry(password_frame, font=("Arial", 12), width=20, state="readonly", bg="#f0f0f0", relief="solid", borderwidth=1)
password_entry.grid(row=0, column=1)

# Buttons Frame
button_frame = tk.Frame(root, bg="#fafafa")
button_frame.pack(pady=20)

generate_button = tk.Button(button_frame, text="Generate Password", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_password, width=16, relief="flat")
generate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear Password", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=clear_password, width=16, relief="flat")
clear_button.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()

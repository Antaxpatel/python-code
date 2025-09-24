import tkinter as tk
from tkinter import messagebox

attempts = 3

def login():
    global attempts
    username = username_entry.get()
    try:
        pin = int(pin_entry.get())
    except ValueError:
        messagebox.showerror("Error", "PIN must be a number")
        return

    if username == "a" and pin == 1234:
        messagebox.showinfo("Success", "Login done")
        root.destroy()
    else:
        attempts -= 1
        if attempts > 0:
            messagebox.showwarning("Failed", f"Invalid credentials. Attempts left: {attempts}")
        else:
            messagebox.showerror("Locked", "Attempts are closed")
            root.destroy()

# GUI setup
root = tk.Tk()
root.title("ATM Login")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="PIN").pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()

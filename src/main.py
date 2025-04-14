# src/main.py

import tkinter as tk
from tkinter import ttk

# --- App Configurations ---
APP_TITLE = "Personal Expense Tracker"
WINDOW_SIZE = "800x600"

def main():
    # Create the main application window
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(WINDOW_SIZE)
    root.resizable(False, False)  # Disable window resizing

    # Optional: Set app icon
    # root.iconbitmap("assets/app_icon.ico")  # Make sure .ico file exists

    # Add a welcome label temporarily
    label = ttk.Label(root, text="Welcome to Personal Expense Tracker!", font=("Arial", 16))
    label.pack(pady=50)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

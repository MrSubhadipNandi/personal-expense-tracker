# src/main.py

import tkinter as tk
from tkinter import ttk
from ui.home_view import HomeView
from ui.add_expense_view import AddExpenseView
from ui.summary_view import SummaryView

# --- App Configurations ---
APP_TITLE = "Personal Expense Tracker"
WINDOW_SIZE = "800x600"

def main():
    # Create the main application window
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(WINDOW_SIZE)
    root.resizable()  # Allow window resizing
    

    # Optional: Set app icon
    # root.iconbitmap("assets/app_icon.ico")  # Make sure .ico file exists

    # Load the HomeView into the window
    view = HomeView(root)
    
    # Load the AddExpenseView into the window
    view = AddExpenseView(root)

    # Load the SummaryView into the window
    view = SummaryView(root)

    # view.pack(fill='both', expand=True)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

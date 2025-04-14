# src/app.py

import tkinter as tk
from tkinter import ttk

from ui.add_expense_view import AddExpenseView
from ui.home_view import HomeView
from ui.summary_view import SummaryView

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties and icon
        self.iconbitmap("assets/icon.ico")
        self.title("Personal Expense Tracker")
        self.geometry("800x600")
        self.resizable()
        
        # --- Navigation Bar ---
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="top", fill="x")

        ttk.Button(nav_frame, text="Add Expense", command=lambda: self.show_frame("AddExpense")).pack(side="left", padx=5, pady=5)
        ttk.Button(nav_frame, text="View Expenses", command=lambda: self.show_frame("Home")).pack(side="left", padx=5, pady=5)
        ttk.Button(nav_frame, text="Summary", command=lambda: self.show_frame("Summary")).pack(side="left", padx=5, pady=5)

        # --- View Container ---
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.frames = {}

        # Initialize views
        for F, name in zip((AddExpenseView, HomeView, SummaryView), ("AddExpense", "Home", "Summary")):
            frame = F(self.container)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")  # Default view

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

# src/ui/home_view.py

import tkinter as tk
from tkinter import ttk
from db.db_handler import get_all_expenses

class HomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text="Expense History", font=("Arial", 16)).pack(pady=10)

        # Treeview setup
        columns = ("id", "date", "category", "amount", "description")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # Refresh button
        ttk.Button(self, text="Refresh", command=self.load_data).pack(pady=10)

        self.load_data()  # Auto-load on view creation

    def load_data(self):
        # Clear old data
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Load from DB
        for row in get_all_expenses():
            self.tree.insert("", "end", values=row)

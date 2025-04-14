# src/ui/home_view.py

import tkinter as tk
from tkinter import ttk, messagebox

class HomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Heading ---
        ttk.Label(self, text="Expense List", font=("Arial", 16)).pack(pady=10)

        # --- Treeview (Expense Table) ---
        self.tree = ttk.Treeview(self, columns=("date", "category", "amount", "description"), show="headings")
        self.tree.heading("date", text="Date")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("description", text="Description")

        self.tree.column("date", width=100)
        self.tree.column("category", width=120)
        self.tree.column("amount", width=80)
        self.tree.column("description", width=200)

        self.tree.pack(pady=10, fill="both", expand=True)

        # --- Buttons ---
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        self.edit_btn = ttk.Button(button_frame, text="Edit", command=self.edit_expense)
        self.edit_btn.grid(row=0, column=0, padx=5)

        self.delete_btn = ttk.Button(button_frame, text="Delete", command=self.delete_expense)
        self.delete_btn.grid(row=0, column=1, padx=5)

        self.filter_btn = ttk.Button(button_frame, text="Filter", command=self.filter_expenses)
        self.filter_btn.grid(row=0, column=2, padx=5)

        # --- Add Dummy Data ---
        self.load_dummy_data()

    def load_dummy_data(self):
        dummy_expenses = [
            ("2025-04-13", "Food", 120.0, "Lunch at cafe"),
            ("2025-04-12", "Transport", 50.0, "Bus ticket"),
            ("2025-04-11", "Shopping", 400.0, "Clothes"),
        ]
        for exp in dummy_expenses:
            self.tree.insert("", "end", values=exp)

    def edit_expense(self):
        messagebox.showinfo("Edit", "Edit functionality coming soon!")

    def delete_expense(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Delete", "No item selected.")
            return
        self.tree.delete(selected_item)

    def filter_expenses(self):
        messagebox.showinfo("Filter", "Filter functionality coming soon!")

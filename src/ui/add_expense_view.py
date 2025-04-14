# src/ui/add_expense_view.py

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AddExpenseView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Form Fields ---
        # Date
        ttk.Label(self, text="Date:").grid(row=0, column=0, sticky="w", pady=5)
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_entry = ttk.Entry(self, textvariable=self.date_var, width=30)
        self.date_entry.grid(row=0, column=1, pady=5)

        # Category
        ttk.Label(self, text="Category:").grid(row=1, column=0, sticky="w", pady=5)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(
            self, textvariable=self.category_var, state="readonly",
            values=["Food", "Transport", "Shopping", "Utilities", "Entertainment", "Other"]
        )
        self.category_dropdown.grid(row=1, column=1, pady=5)
        self.category_dropdown.set("Select Category")

        # Amount
        ttk.Label(self, text="Amount (₹):").grid(row=2, column=0, sticky="w", pady=5)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(self, textvariable=self.amount_var, width=30)
        self.amount_entry.grid(row=2, column=1, pady=5)

        # Description
        ttk.Label(self, text="Description:").grid(row=3, column=0, sticky="w", pady=5)
        self.description_var = tk.StringVar()
        self.description_entry = ttk.Entry(self, textvariable=self.description_var, width=30)
        self.description_entry.grid(row=3, column=1, pady=5)

        # Submit Button
        self.submit_btn = ttk.Button(self, text="Add Expense", command=self.add_expense)
        self.submit_btn.grid(row=4, column=0, columnspan=2, pady=15)

        # Configure grid spacing
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

    def add_expense(self):
        # Simple validation
        date = self.date_var.get()
        category = self.category_var.get()
        amount = self.amount_var.get()
        description = self.description_var.get()

        if category == "Select Category" or not amount:
            messagebox.showerror("Input Error", "Please enter category and amount.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
            return

        # Just print for now (DB comes in later)
        print("Date:", date)
        print("Category:", category)
        print("Amount:", amount)
        print("Description:", description)
        messagebox.showinfo("Success", "Expense added (not saved yet!)")

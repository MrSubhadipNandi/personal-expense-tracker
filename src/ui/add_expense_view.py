# src/ui/add_expense_view.py

import tkinter as tk
from tkinter import ttk, messagebox
from db.db_handler import insert_expense
from datetime import datetime

class AddExpenseView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self, text="Add New Expense", font=("Arial", 16)).pack(pady=10)

        form = ttk.Frame(self)
        form.pack(pady=10)

        # --- Form Fields ---
        ttk.Label(form, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="e")
        self.date_entry = ttk.Entry(form)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.today().strftime("%Y-%m-%d"))

        ttk.Label(form, text="Category:").grid(row=1, column=0, sticky="e")
        self.category_entry = ttk.Entry(form)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text="Amount:").grid(row=2, column=0, sticky="e")
        self.amount_entry = ttk.Entry(form)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text="Description:").grid(row=3, column=0, sticky="e")
        self.description_entry = ttk.Entry(form)
        self.description_entry.grid(row=3, column=1, padx=5, pady=5)

        # --- Save Button ---
        ttk.Button(self, text="Save Expense", command=self.save_expense).pack(pady=15)

    def save_expense(self):
        date = self.date_entry.get().strip()
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()
        description = self.description_entry.get().strip()

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")
            return

        if not (date and category and amount):
            messagebox.showerror("Missing Data", "Please fill all required fields.")
            return

        insert_expense(date, category, amount, description)
        messagebox.showinfo("Saved", "Expense added successfully!")

        self.clear_form()

    def clear_form(self):
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.today().strftime("%Y-%m-%d"))
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

# src/ui/home_view.py

import tkinter as tk 
from tkinter import messagebox, ttk
from db.db_handler import get_all_expenses, update_expense, delete_expense

class HomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ttk.Label(self, text="Expense History", font=("Arial", 16)).pack(pady=10)

        columns = ("id", "date", "category", "amount", "description")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True, pady=5)


        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Refresh", command=self.load_data).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Edit Selected", command=self.edit_selected).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).grid(row=0, column=2, padx=5)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in get_all_expenses():
            self.tree.insert("", "end", values=row)

    def get_selected_row(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an expense row.")
            return None
        return self.tree.item(selected[0])["values"]

    def delete_selected(self):
        row = self.get_selected_row()
        if not row: return

        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this expense?")
        if confirm:
            delete_expense(row[0])
            self.load_data()

    def edit_selected(self):
        row = self.get_selected_row()
        if not row: return

        EditPopup(self, row, self.load_data)


class EditPopup(tk.Toplevel):
    def __init__(self, parent, row_data, refresh_callback):
        super().__init__(parent)
        self.title("Edit Expense")
        self.geometry("300x250")
        self.refresh_callback = refresh_callback

        self.expense_id = row_data[0]

        ttk.Label(self, text="Date:").pack(pady=5)
        self.date_entry = ttk.Entry(self)
        self.date_entry.pack()
        self.date_entry.insert(0, row_data[1])

        ttk.Label(self, text="Category:").pack(pady=5)
        self.category_entry = ttk.Entry(self)
        self.category_entry.pack()
        self.category_entry.insert(0, row_data[2])

        ttk.Label(self, text="Amount:").pack(pady=5)
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.pack()
        self.amount_entry.insert(0, row_data[3])

        ttk.Label(self, text="Description:").pack(pady=5)
        self.description_entry = ttk.Entry(self)
        self.description_entry.pack()
        self.description_entry.insert(0, row_data[4])

        ttk.Button(self, text="Save Changes", command=self.save).pack(pady=10)

    def save(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")
            return

        update_expense(
            self.expense_id,
            self.date_entry.get(),
            self.category_entry.get(),
            amount,
            self.description_entry.get()
        )

        messagebox.showinfo("Saved", "Expense updated successfully!")
        self.refresh_callback()
        self.destroy()

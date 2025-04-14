# src/ui/summary_view.py

import tkinter as tk
from tkinter import ttk
from db.db_handler import get_all_expenses

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

class SummaryView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text="Expense Summary", font=("Arial", 16)).pack(pady=10)

        # Create container for chart
        self.chart_frame = ttk.Frame(self)
        self.chart_frame.pack(fill="both", expand=True)

        ttk.Button(self, text="Refresh Chart", command=self.load_chart).pack(pady=10)

        self.load_chart()

    def load_chart(self):
        # Clear old chart (if any)
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Aggregate data
        expenses = get_all_expenses()
        category_totals = defaultdict(float)

        for _, _, category, amount, _ in expenses:
            category_totals[category] += float(amount)

        if not category_totals:
            ttk.Label(self.chart_frame, text="No data to display.", foreground="gray").pack()
            return

        # Plot chart
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        ax.pie(
            category_totals.values(),
            labels=category_totals.keys(),
            autopct="%1.1f%%",
            startangle=140
        )
        ax.set_title("Spending by Category")

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

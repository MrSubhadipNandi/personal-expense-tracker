# src/ui/summary_view.py

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class SummaryView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self, text="Expense Summary", font=("Arial", 16)).pack(pady=10)

        chart_frame = ttk.Frame(self)
        chart_frame.pack(fill="both", expand=True)

        self.draw_category_pie_chart(chart_frame)
        self.draw_daily_bar_chart(chart_frame)

    def draw_category_pie_chart(self, parent):
        # Dummy data: category and total spent
        categories = ["Food", "Transport", "Shopping", "Utilities", "Entertainment"]
        amounts = [300, 150, 400, 120, 180]

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.set_title("Category-wise Spending")

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill="both", expand=True, padx=10, pady=10)

    def draw_daily_bar_chart(self, parent):
        # Dummy data: date and amount spent
        dates = ["Apr 10", "Apr 11", "Apr 12", "Apr 13"]
        amounts = [250, 400, 180, 320]

        fig, ax = plt.subplots(figsize=(4.5, 4))
        ax.bar(dates, amounts, color="skyblue")
        ax.set_ylabel("Amount (₹)")
        ax.set_title("Daily Spending Trends")

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="right", fill="both", expand=True, padx=10, pady=10)

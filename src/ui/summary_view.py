# src/ui/summary_view.py

import tkinter as tk
from tkinter import ttk

class SummaryView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="Summary View")
        label.pack(padx=10, pady=10)

# src/ui/home_view.py

import tkinter as tk
from tkinter import ttk

class HomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="Home View")
        label.pack(padx=10, pady=10)

# 💰 Personal Expense Tracker

A desktop application built with Python and Tkinter to help you manage and track your daily expenses effectively.

---

## 🚀 Features

- Add, edit, and delete expense entries
- View expenses by day, week, or month
- Filter by category
- SQLite-based persistent storage
- Visual summary with charts (matplotlib)
- Export data to CSV
- User-friendly GUI with Tkinter

---

## 🖼️ Screenshots

> *(screenshots here as you build the UI)*

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **GUI Framework:** Tkinter (`ttk` for styling)  
- **Database:** SQLite3  
- **Visualization:** Matplotlib  
- **Export:** CSV module

---

## 📂 Project Structure

```
personal-expense-tracker/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── assets/                      # Icons, images, logos
│   └── app_icon.ico
│
├── data/                        # DB file and exported CSVs
│   ├── expenses.db
│   └── export.csv
│
├── src/                         # Source code
│   ├── __init__.py
│   ├── main.py                  # App entry point
│
│   ├── ui/                      # UI layouts, windows, styling
│   │   ├── __init__.py
│   │   ├── home_view.py
│   │   ├── add_expense_view.py
│   │   ├── summary_view.py
│   │   └── components.py        # Reusable widgets
│
│   ├── db/                      # Database-related code
│   │   ├── __init__.py
│   │   └── db_manager.py        # DB connection, CRUD
│
│   ├── utils/                   # Helper functions, validators
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── date_helpers.py
│
├── tests/                       # Unit and functional tests
│   ├── __init__.py
│   ├── test_db.py
│   ├── test_validators.py
│   └── test_ui_basic.py


```
# src/main.py

from app import App
from db.db_handler import init_db

def main():
    init_db()
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()

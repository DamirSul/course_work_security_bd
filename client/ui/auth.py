# ui/auth.py

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from .main_app import FlowerApp

BASE_URL = "http://localhost:8000"

def login_window():
    def authenticate():
        code = code_entry.get()
        try:
            resp = requests.post(f"{BASE_URL}/auth/login", json={"code": code})
            if resp.status_code == 200:
                login_win.destroy()
                user = resp.json()
                root = tk.Tk()
                app = FlowerApp(root, user)
                root.mainloop()
            else:
                messagebox.showerror("Ошибка", "Неверный код")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    login_win = tk.Tk()
    login_win.title("Авторизация")

    ttk.Label(login_win, text="Код доступа").pack()
    code_entry = ttk.Entry(login_win)
    code_entry.pack()

    ttk.Button(login_win, text="Войти", command=authenticate).pack()

    login_win.mainloop()
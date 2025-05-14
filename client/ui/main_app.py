# ui/main_app.py

import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = "http://localhost:8000"

class FlowerApp:
    def __init__(self, root, user):
        self.user = user
        self.root = root
        self.root.title("ИС Хозяйства по выращиванию цветов")

        tab_control = ttk.Notebook(root)

        if user['role'] in ['admin', 'operator', 'agronomist']:
            self.init_beds_tab(tab_control)
            self.init_bed_actions_tab(tab_control)
            self.init_planting_summary_tab(tab_control)
            self.init_beds_fill_tab(tab_control)

        if user['role'] in ['admin', 'operator']:
            self.init_employees_tab(tab_control)
            self.init_resources_tab(tab_control)
            self.init_planting_tab(tab_control)
            self.init_flower_base_tab(tab_control)
            self.init_purchase_plans_tab(tab_control)
            self.init_purchases_tab(tab_control)
            self.init_agronomists_tab(tab_control)

        if user['role'] == 'admin':
            self.init_report_tab(tab_control)

        tab_control.pack(expand=1, fill="both")

        logout_button = ttk.Button(root, text="Выход", command=self.logout)
        logout_button.pack(pady=10)

    def logout(self):
        self.root.destroy()
        from ui.auth import login_window
        login_window()

    def init_employees_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Сотрудники')
        ttk.Label(tab, text="Список сотрудников").pack()
        self.emp_listbox = tk.Listbox(tab, width=80)
        self.emp_listbox.pack()
        ttk.Button(tab, text="Загрузить", command=self.load_employees).pack()

    def init_resources_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Ресурсы')
        ttk.Label(tab, text="Список ресурсов").pack()
        self.res_listbox = tk.Listbox(tab, width=80)
        self.res_listbox.pack()
        ttk.Button(tab, text="Обновить", command=self.load_resources).pack()

    def init_planting_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Посадки')
        ttk.Label(tab, text="ID Цветка").pack()
        self.flower_id_entry = ttk.Entry(tab)
        self.flower_id_entry.pack()
        ttk.Label(tab, text="ID Грядки").pack()
        self.bed_id_entry = ttk.Entry(tab)
        self.bed_id_entry.pack()
        ttk.Label(tab, text="Количество для посадки").pack()
        self.qty_entry = ttk.Entry(tab)
        self.qty_entry.pack()
        ttk.Button(tab, text="Посадить", command=self.plant_flower).pack()

    def init_report_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Отчетность')
        ttk.Button(tab, text="Сформировать отчет", command=self.generate_report).pack()

    def init_beds_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Грядки')
        ttk.Label(tab, text="Список грядок").pack()
        self.beds_listbox = tk.Listbox(tab, width=80)
        self.beds_listbox.pack()
        ttk.Button(tab, text="Показать", command=self.load_beds).pack()

    def init_bed_actions_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='История грядок')
        ttk.Label(tab, text="История действий на грядках").pack()
        self.actions_listbox = tk.Listbox(tab, width=100)
        self.actions_listbox.pack()
        ttk.Button(tab, text="Обновить", command=self.load_bed_actions).pack()

    def init_planting_summary_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Сводка посадок')
        self.planting_summary = tk.Listbox(tab, width=100)
        self.planting_summary.pack()
        ttk.Button(tab, text="Показать", command=self.load_planting_summary).pack()

    def init_flower_base_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='База растений')
        self.flower_list = tk.Listbox(tab, width=100)
        self.flower_list.pack()
        ttk.Button(tab, text="Загрузить", command=self.load_flower_base).pack()

    def init_beds_fill_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Заполненность грядок')
        self.fill_list = tk.Listbox(tab, width=100)
        self.fill_list.pack()
        ttk.Button(tab, text="Показать", command=self.load_beds).pack()

    def init_purchase_plans_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Планы закупок')
        self.plan_list = tk.Listbox(tab, width=100)
        self.plan_list.pack()
        ttk.Button(tab, text="Загрузить", command=self.load_purchase_plans).pack()

    def init_purchases_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Заявки на ресурсы')
        self.purchases_list = tk.Listbox(tab, width=100)
        self.purchases_list.pack()
        ttk.Button(tab, text="Обновить", command=self.load_purchases).pack()

    def init_agronomists_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Агрономы')
        self.agronomist_list = tk.Listbox(tab, width=100)
        self.agronomist_list.pack()
        ttk.Button(tab, text="Показать", command=self.load_agronomists).pack()

    def load_employees(self):
        try:
            response = requests.get(f"{BASE_URL}/employees/")
            self.emp_listbox.delete(0, tk.END)
            for emp in response.json():
                self.emp_listbox.insert(tk.END, f"{emp['id']} | {emp['full_name']} | {emp['position']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_resources(self):
        try:
            response = requests.get(f"{BASE_URL}/resources/")
            self.res_listbox.delete(0, tk.END)
            for res in response.json():
                self.res_listbox.insert(tk.END, f"{res['id']} | {res['resource_name']} | {res['quantity_available']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_bed_actions(self):
        try:
            response = requests.get(f"{BASE_URL}/beds/actions")
            self.actions_listbox.delete(0, tk.END)
            for action in response.json():
                self.actions_listbox.insert(tk.END, str(action))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_planting_summary(self):
        try:
            response = requests.get(f"{BASE_URL}/plantings/summary")
            self.planting_summary.delete(0, tk.END)
            for row in response.json():
                self.planting_summary.insert(tk.END, str(row))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_flower_base(self):
        try:
            response = requests.get(f"{BASE_URL}/flowers/")
            self.flower_list.delete(0, tk.END)
            for flower in response.json():
                self.flower_list.insert(tk.END, f"{flower['id']} | {flower['flower_name']} | {flower['variety']} | {flower['color']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_purchase_plans(self):
        try:
            response = requests.get(f"{BASE_URL}/purchase_plan/pending")
            self.plan_list.delete(0, tk.END)
            for plan in response.json():
                self.plan_list.insert(tk.END, str(plan))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_purchases(self):
        try:
            response = requests.get(f"{BASE_URL}/purchases/")
            self.purchases_list.delete(0, tk.END)
            for p in response.json():
                self.purchases_list.insert(tk.END, str(p))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_agronomists(self):
        try:
            response = requests.get(f"{BASE_URL}/agronomists/")
            self.agronomist_list.delete(0, tk.END)
            for agr in response.json():
                self.agronomist_list.insert(tk.END, f"{agr['id']} | {agr['full_name']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def plant_flower(self):
        data = {
            "flower_id": int(self.flower_id_entry.get()),
            "bed_id": int(self.bed_id_entry.get()),
            "action_id": 1,
            "quantity_planted": int(self.qty_entry.get())
        }
        try:
            response = requests.post(f"{BASE_URL}/flower_planting/", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Успех", "Цветы посажены")
            else:
                messagebox.showerror("Ошибка", response.text)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def generate_report(self):
        try:
            response = requests.get(f"{BASE_URL}/report/summary")
            messagebox.showinfo("Отчет", response.json().get("message", "Нет ответа"))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_beds(self):
        try:
            response = requests.get(f"{BASE_URL}/beds/")
            self.beds_listbox.delete(0, tk.END)
            for bed in response.json():
                self.beds_listbox.insert(tk.END, f"{bed['id']} | {bed['bed_name']} | {bed['current_occupancy']} / {bed['total_capacity']}")
            if hasattr(self, 'fill_list'):
                self.fill_list.delete(0, tk.END)
                for bed in response.json():
                    self.fill_list.insert(tk.END, f"{bed['id']} | {bed['bed_name']} | {bed['current_occupancy']} / {bed['total_capacity']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

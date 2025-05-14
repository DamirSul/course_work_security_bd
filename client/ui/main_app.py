# ui/main_app.py

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import date

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
            self.init_resources_tab(tab_control)
            self.init_planting_tab(tab_control)
            self.init_flower_base_tab(tab_control)
            self.init_purchase_plans_tab(tab_control)
            self.init_purchases_tab(tab_control)
            self.init_agronomists_tab(tab_control)

        if user['role'] == 'admin':
            self.init_employees_tab(tab_control)
            self.init_add_employee_tab(tab_control)
            self.init_add_bed_tab(tab_control)
            self.init_add_agronomist_tab(tab_control)

        if user['role'] in ['admin', 'operator']:
            self.init_add_purchase_plan_tab(tab_control)

        if user['role'] == 'admin':
            self.init_report_tab(tab_control)

        tab_control.pack(expand=1, fill="both")

        logout_button = ttk.Button(root, text="Выход", command=self.logout)
        logout_button.pack(pady=10)



    def init_report_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Отчетность')
        ttk.Label(tab, text="Формирование отчета по предприятию").pack()
        ttk.Button(tab, text="Сформировать отчет", command=self.generate_report).pack()

    def generate_report(self):
        try:
            response = requests.get(f"{BASE_URL}/report/summary")
            messagebox.showinfo("Отчет", response.json().get("message", "Нет ответа"))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

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

    def init_flower_base_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='База растений')
        self.flower_list = tk.Listbox(tab, width=100)
        self.flower_list.pack()
        ttk.Button(tab, text="Загрузить", command=self.load_flower_base).pack()

    def load_flower_base(self):
        try:
            response = requests.get(f"{BASE_URL}/flowers/")
            self.flower_list.delete(0, tk.END)
            for flower in response.json():
                self.flower_list.insert(tk.END, f"{flower['id']} | {flower['flower_name']} | {flower['variety']} | {flower['color']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_purchase_plans_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Планы закупок')
        self.plan_list = tk.Listbox(tab, width=100)
        self.plan_list.pack()
        ttk.Button(tab, text="Загрузить", command=self.load_purchase_plans).pack()

    def load_purchase_plans(self):
        try:
            response = requests.get(f"{BASE_URL}/purchase_plan/pending")
            self.plan_list.delete(0, tk.END)
            for plan in response.json():
                self.plan_list.insert(tk.END, str(plan))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_purchases_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Заявки на ресурсы')
        self.purchases_list = tk.Listbox(tab, width=100)
        self.purchases_list.pack()
        ttk.Button(tab, text="Обновить", command=self.load_purchases).pack()

    def load_purchases(self):
        try:
            response = requests.get(f"{BASE_URL}/purchases/")
            self.purchases_list.delete(0, tk.END)
            for p in response.json():
                self.purchases_list.insert(tk.END, str(p))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_agronomists_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Агрономы')
        self.agronomist_list = tk.Listbox(tab, width=100)
        self.agronomist_list.pack()
        ttk.Button(tab, text="Показать", command=self.load_agronomists).pack()

    def load_agronomists(self):
        try:
            response = requests.get(f"{BASE_URL}/agronomists/")
            self.agronomist_list.delete(0, tk.END)
            for agr in response.json():
                self.agronomist_list.insert(tk.END, f"{agr['id']} | {agr['full_name']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_beds_fill_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Заполненность грядок')
        ttk.Label(tab, text="Заполненность грядок").pack()
        self.fill_list = tk.Listbox(tab, width=100)
        self.fill_list.pack()
        ttk.Button(tab, text="Показать", command=self.load_beds_fill).pack()

    def load_beds_fill(self):
        try:
            response = requests.get(f"{BASE_URL}/beds/")
            self.fill_list.delete(0, tk.END)
            for bed in response.json():
                self.fill_list.insert(
                    tk.END,
                    f"{bed['id']} | {bed['bed_name']} | {bed['current_occupancy']} / {bed['total_capacity']}"
                )
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_resources_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Ресурсы')
        ttk.Label(tab, text="Список ресурсов").pack()
        self.res_listbox = tk.Listbox(tab, width=80)
        self.res_listbox.pack()
        ttk.Button(tab, text="Обновить", command=self.load_resources).pack()

    def load_resources(self):
        try:
            response = requests.get(f"{BASE_URL}/resources/")
            resources = response.json()

            # Словарь по наименованию
            resources_by_name = {res["resource_name"]: res["quantity_available"] for res in resources}

            self.res_listbox.delete(0, tk.END)

            # Показываем фиксированные 3 ресурса
            for name in ["Удобрения", "Средства защиты", "Доп средства"]:
                quantity = resources_by_name.get(name, 0)
                self.res_listbox.insert(tk.END, f"{name}: {quantity} / 100")

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))



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

    def load_employees(self):
        try:
            role_value = self.user.get("role")

            headers = {"X-Role": role_value}

            response = requests.get(f"{BASE_URL}/employees/", headers=headers)

            if response.status_code != 200:
                raise Exception(response.json().get("detail", "Ошибка доступа"))

            self.emp_listbox.delete(0, tk.END)
            for emp in response.json():
                self.emp_listbox.insert(tk.END, f"{emp['id']} | {emp['full_name']} | {emp['position']}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))



    def init_add_employee_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Добавить сотрудника')
        self.fullname_entry = ttk.Entry(tab)
        self.position_entry = ttk.Entry(tab)
        self.phone_entry = ttk.Entry(tab)
        ttk.Label(tab, text="ФИО").pack()
        self.fullname_entry.pack()
        ttk.Label(tab, text="Должность").pack()
        self.position_entry.pack()
        ttk.Label(tab, text="Телефон").pack()
        self.phone_entry.pack()
        ttk.Button(tab, text="Добавить", command=self.add_employee).pack()

    def add_employee(self):
        data = {
            "full_name": self.fullname_entry.get(),
            "position": self.position_entry.get(),
            "phone_number": self.phone_entry.get()
        }
        try:
            resp = requests.post(f"{BASE_URL}/employees/", json=data)
            if resp.status_code == 200:
                messagebox.showinfo("Успех", "Сотрудник добавлен")
            else:
                messagebox.showerror("Ошибка", resp.text)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_add_bed_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Добавить грядку')
        self.bed_name_entry = ttk.Entry(tab)
        self.capacity_entry = ttk.Entry(tab)
        ttk.Label(tab, text="Название грядки").pack()
        self.bed_name_entry.pack()
        ttk.Label(tab, text="Вместимость").pack()
        self.capacity_entry.pack()
        ttk.Button(tab, text="Добавить", command=self.add_bed).pack()

    def add_bed(self):
        data = {
            "bed_name": self.bed_name_entry.get(),
            "total_capacity": int(self.capacity_entry.get()),
            "current_occupancy": 0
        }
        try:
            resp = requests.post(f"{BASE_URL}/beds/", json=data)
            if resp.status_code == 200:
                messagebox.showinfo("Успех", "Грядка добавлена")
            else:
                messagebox.showerror("Ошибка", resp.text)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_add_purchase_plan_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Создать план закупки')
        self.res_id_entry = ttk.Entry(tab)
        self.qty_entry = ttk.Entry(tab)
        ttk.Label(tab, text="ID ресурса").pack()
        self.res_id_entry.pack()
        ttk.Label(tab, text="Количество").pack()
        self.qty_entry.pack()
        ttk.Button(tab, text="Создать", command=self.add_purchase_plan).pack()

    def add_purchase_plan(self):
        data = {
            "resource_id": int(self.res_id_entry.get()),
            "quantity": int(self.qty_entry.get()),
            "employee_id": self.user['id'],
            "create_date": date.today().isoformat()
        }
        try:
            resp = requests.post(f"{BASE_URL}/purchase_plan/", json=data)
            if resp.status_code == 200:
                messagebox.showinfo("Успех", "План создан")
            else:
                messagebox.showerror("Ошибка", resp.text)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_add_agronomist_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Назначить агронома')
        self.agronomist_emp_entry = ttk.Entry(tab)
        ttk.Label(tab, text="ID сотрудника").pack()
        self.agronomist_emp_entry.pack()
        ttk.Button(tab, text="Назначить", command=self.assign_agronomist).pack()

    def assign_agronomist(self):
        data = {
            "employee_id": int(self.agronomist_emp_entry.get())
        }
        try:
            resp = requests.post(f"{BASE_URL}/agronomists/", json=data)
            if resp.status_code == 200:
                messagebox.showinfo("Успех", "Агроном назначен")
            else:
                messagebox.showerror("Ошибка", resp.text)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def init_bed_actions_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='История грядок')
        ttk.Label(tab, text="История действий на грядках").pack()
        self.actions_listbox = tk.Listbox(tab, width=100)
        self.actions_listbox.pack()
        ttk.Button(tab, text="Обновить", command=self.load_bed_actions).pack()

    def load_bed_actions(self):
        try:
            response = requests.get(f"{BASE_URL}/beds/actions")
            self.actions_listbox.delete(0, tk.END)
            for action in response.json():
                self.actions_listbox.insert(tk.END, str(action))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def init_beds_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Грядки')
        ttk.Label(tab, text="Список грядок").pack()
        self.beds_listbox = tk.Listbox(tab, width=80)
        self.beds_listbox.pack()
        ttk.Button(tab, text="Показать", command=self.load_beds).pack()

    def load_beds(self):
        try:
            response = requests.get(f"{BASE_URL}/beds/")
            self.beds_listbox.delete(0, tk.END)
            for bed in response.json():
                self.beds_listbox.insert(
                    tk.END,
                    f"{bed['id']} | {bed['bed_name']} | {bed['current_occupancy']} / {bed['total_capacity']}"
                )
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    
    def init_planting_summary_tab(self, parent):
        tab = ttk.Frame(parent)
        parent.add(tab, text='Сводка посадок')
        ttk.Label(tab, text="Сводка по посадкам").pack()
        self.planting_summary_listbox = tk.Listbox(tab, width=100)
        self.planting_summary_listbox.pack()
        ttk.Button(tab, text="Обновить", command=self.load_planting_summary).pack()

    def load_planting_summary(self):
        try:
            response = requests.get(f"{BASE_URL}/plantings/summary")
            self.planting_summary_listbox.delete(0, tk.END)
            for planting in response.json():
                self.planting_summary_listbox.insert(tk.END, str(planting))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


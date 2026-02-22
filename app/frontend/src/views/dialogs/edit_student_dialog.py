import tkinter as tk
from tkinter import messagebox, ttk

class UpdateStudentDialog:
    def __init__(self, parent, controller, student_data):
        self.controller = controller
        self.result = None

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Edit Student")
        self.dialog.geometry("400x400")
        self.dialog.resizable(False, False)
        self.dialog.grab_set()

        tk.Label(self.dialog, text="Edit Student", font=("Arial", 14, "bold")).pack(pady=10)

        form = tk.Frame(self.dialog)
        form.pack(padx=20, pady=10, fill="x")

        tk.Label(form, text="ID Number:").grid(row=0, column=0, sticky="w", pady=5)
        self.id_entry = tk.Entry(form)
        self.id_entry.insert(0, student_data['ID Number'])  # ← dict key
        self.id_entry.config(state="disabled")
        self.id_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(form, text="Name:").grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(form)
        self.name_entry.insert(0, student_data['Name'])  # ← dict key
        self.name_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(form, text="Gender:").grid(row=2, column=0, sticky="w", pady=5)
        self.gender_var = tk.StringVar(value=student_data['Gender'])  # ← dict key
        tk.Radiobutton(form, text="Male", variable=self.gender_var, value="Male").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(form, text="Female", variable=self.gender_var, value="Female").grid(row=2, column=1)

        tk.Label(form, text="Year Level:").grid(row=3, column=0, sticky="w", pady=5)
        self.year_entry = tk.Entry(form)
        self.year_entry.insert(0, student_data['Year Level'])  # ← dict key
        self.year_entry.grid(row=3, column=1, sticky="ew")

        tk.Label(form, text="Program:").grid(row=4, column=0, sticky="w", pady=5)
        self.program_entry = tk.Entry(form)
        self.program_entry.insert(0, student_data['Program'])  # ← dict key
        self.program_entry.grid(row=4, column=1, sticky="ew")

        tk.Label(form, text="College:").grid(row=5, column=0, sticky="w", pady=5)
        self.college_entry = tk.Entry(form)
        self.college_entry.insert(0, student_data['College'])  # ← dict key
        self.college_entry.grid(row=5, column=1, sticky="ew")

        btn_frame = tk.Frame(self.dialog)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Save", command=self.on_save, bg="#85586F", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.dialog.destroy, width=10).pack(side="left", padx=5)

    def on_save(self):
        self.id_entry.config(state="normal")   # ← temporarily enable to read
        id_value = self.id_entry.get()
        self.id_entry.config(state="disabled") # ← lock again

        student_data = {
            'ID Number': id_value,
            'Name': self.name_entry.get().strip(),
            'Gender': self.gender_var.get(),
            'Year Level': self.year_entry.get(),
            'Program': self.program_entry.get().strip(),
            'College': self.college_entry.get().strip()
        }

        if not all(student_data.values()):
            messagebox.showwarning("Incomplete", "Please fill in all fields.")
            return

        self.controller.update_student(student_data)
        self.dialog.destroy()
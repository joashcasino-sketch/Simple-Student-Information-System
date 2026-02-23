import tkinter as tk
from tkinter import messagebox, ttk

class UpdateProgramDialog:
    def __init__(self, parent, controller, student_data):
        self.controller = controller
        self.result = None

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Edit Student")
        self.dialog.geometry("400x500")
        self.dialog.configure(bg="#F8ECD1")
        self.dialog.resizable(False, False)
        self.dialog.grab_set()

        title = tk.Label(
            self.dialog,
            text="Edit Student",
            font=("Lato", 16, "bold"),
            background="#85586F",
            foreground="white",
            pady=15
        )
        title.pack(fill="x")

        # tk.Label(self.dialog, text="Edit Student", font=("Arial", 14, "bold")).pack(pady=10)

        form = tk.Frame(self.dialog, padx=30, pady=20, bg="#F8ECD1")
        form.pack(padx=20, pady=10, fill="x")

        tk.Label(form, background="#F8ECD1", text="ID Number:", font=("Lato", 10)).grid(row=0, column=0, sticky="w", pady=10)
        self.id_entry = tk.Entry(form)
        self.id_entry.insert(0, student_data['ID Number'])  # ← dict key
        self.id_entry.config(bg="#DEB6AB", state="disabled")
        self.id_entry.grid(row=0, column=1, pady=10)

        tk.Label(form, background="#F8ECD1", text="Name:", font=("Lato", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(form,  bg="#DEB6AB", font=("Lato", 10), width=30)
        self.name_entry.insert(0, student_data['Name'])  # ← dict key
        self.name_entry.grid(row=1, column=1, pady=10)

        tk.Label(form, background="#F8ECD1", text="Gender:", font=("Lato", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.gender_var = tk.StringVar(value=student_data['Gender'])  # ← dict key
        tk.Radiobutton(form, bg="#F8ECD1", text="Male", variable=self.gender_var, value="Male").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(form, bg="#F8ECD1", text="Female", variable=self.gender_var, value="Female").grid(row=2, column=1)

        tk.Label(form, background="#F8ECD1", text="Year Level:", font=("Lato", 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.year_var = tk.StringVar(value='1')
        year_dropdown = tk.OptionMenu(form, self.year_var, "1", "2", "3", "4")
        year_dropdown.config(width=27, bg="#DEB6AB")
        year_dropdown.grid(row=3, column=1, pady=10)
        
        # self.year_entry.insert(0, student_data['Year Level'])  # ← dict key
        # self.year_entry.grid(row=3, column=1, sticky="ew")

        tk.Label(form, background="#F8ECD1", text="Program:", font=("Lato", 10)).grid(row=4, column=0, sticky="w", pady=5)
        self.program_entry = tk.Entry(form, bg="#DEB6AB", font=("Lato", 10), width=30)
        self.program_entry.insert(0, student_data['Program'])  # ← dict key
        self.program_entry.grid(row=4, column=1, pady=10)

        tk.Label(form, background="#F8ECD1", text="College:", font=("Lato", 10)).grid(row=5, column=0, sticky="w", pady=5)
        self.college_entry = tk.Entry(form, bg="#DEB6AB", font=("Lato", 10), width=30)
        self.college_entry.insert(0, student_data['College'])  # ← dict key
        self.college_entry.grid(row=5, column=1, pady=10)

        btn_frame = tk.Frame(self.dialog, bg="#F8ECD1",pady=20)
        btn_frame.pack()
        save_button = tk.Button(btn_frame,
                text="Save",
                font=("Lato", 10, "bold"),
                bg="#85586F", 
                fg="white",
                width=12,
                command=self.on_save,
                cursor="hand2"
        )
        save_button.pack(side="left", padx=10)

        cancel_button = tk.Button(btn_frame,
                text="Cancel",
                font=("Lato", 10, "bold"),
                bg="#D3D3D3", 
                fg="black",
                width=12,
                command=self.dialog.destroy,
                cursor="hand2"
        )
        cancel_button.pack(side="left", padx=10)
        
        # tk.Button(btn_frame, text="Cancel", command=self.dialog.destroy, width=10).pack(side="left", padx=5)

        self.dialog.transient(parent)
        self._center_window()

    def _center_window(self):
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (self.dialog.winfo_width() // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (self.dialog.winfo_height() // 2)
        self.dialog.geometry(f'+{x}+{y}')

    

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
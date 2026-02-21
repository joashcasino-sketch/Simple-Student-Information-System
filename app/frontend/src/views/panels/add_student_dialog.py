import tkinter as tk
from tkinter import messagebox

class AddStudentDialog:
    def __init__(self, parent, controller):
        self.controller = controller
        self.result = None
        
        # Create toplevel window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Student")
        self.dialog.geometry("400x500")
        self.dialog.resizable(False, False)
        self.dialog.grab_set()  # Make it modal
        
        self._create_widgets()
        
        # Center the window
        self.dialog.transient(parent)
        self._center_window()
    
    def _center_window(self):
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (self.dialog.winfo_width() // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (self.dialog.winfo_height() // 2)
        self.dialog.geometry(f'+{x}+{y}')
    
    def _create_widgets(self):
        # Title
        title = tk.Label(
            self.dialog,
            text="Add New Student",
            font=("Lato", 16, "bold"),
            background="#85586F",
            foreground="white",
            pady=15
        )
        title.pack(fill="x")
        
        # Form frame
        form_frame = tk.Frame(self.dialog, padx=30, pady=20)
        form_frame.pack(fill="both", expand=True)
        
        # ID Number
        tk.Label(form_frame, text="ID Number:", font=("Lato", 10)).grid(row=0, column=0, sticky="w", pady=10)
        self.id_entry = tk.Entry(form_frame, font=("Lato", 10), width=30)
        self.id_entry.grid(row=0, column=1, pady=10)
        
        # Name
        tk.Label(form_frame, text="Name:", font=("Lato", 10)).grid(row=1, column=0, sticky="w", pady=10)
        self.name_entry = tk.Entry(form_frame, font=("Lato", 10), width=30)
        self.name_entry.grid(row=1, column=1, pady=10)
        
        # Gender
        tk.Label(form_frame, text="Gender:", font=("Lato", 10)).grid(row=2, column=0, sticky="w", pady=10)
        self.gender_var = tk.StringVar(value="Male")
        gender_frame = tk.Frame(form_frame)
        gender_frame.grid(row=2, column=1, sticky="w", pady=10)
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male").pack(side="left")
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female").pack(side="left")
        
        # Year Level
        tk.Label(form_frame, text="Year Level:", font=("Lato", 10)).grid(row=3, column=0, sticky="w", pady=10)
        self.year_var = tk.StringVar(value="1")
        year_dropdown = tk.OptionMenu(form_frame, self.year_var, "1", "2", "3", "4")
        year_dropdown.config(width=27)
        year_dropdown.grid(row=3, column=1, pady=10)
        
        # Program
        tk.Label(form_frame, text="Program:", font=("Lato", 10)).grid(row=4, column=0, sticky="w", pady=10)
        self.program_entry = tk.Entry(form_frame, font=("Lato", 10), width=30)
        self.program_entry.grid(row=4, column=1, pady=10)
        
        # College
        tk.Label(form_frame, text="College:", font=("Lato", 10)).grid(row=5, column=0, sticky="w", pady=10)
        self.college_entry = tk.Entry(form_frame, font=("Lato", 10), width=30)
        self.college_entry.grid(row=5, column=1, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.dialog, pady=20)
        button_frame.pack()
        
        # Save button
        save_btn = tk.Button(
            button_frame,
            text="Save",
            font=("Lato", 10, "bold"),
            background="#85586F",
            foreground="white",
            width=12,
            command=self._on_save,
            cursor="hand2"
        )
        save_btn.pack(side="left", padx=10)
        
        # Cancel button
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            font=("Lato", 10, "bold"),
            background="#D3D3D3",
            foreground="black",
            width=12,
            command=self.dialog.destroy,
            cursor="hand2"
        )
        cancel_btn.pack(side="left", padx=10)
    
    def _on_save(self):
        # Collect form data
        student_data = {
            'ID Number': self.id_entry.get().strip(),
            'Name': self.name_entry.get().strip(),
            'Gender': self.gender_var.get(),
            'Year Level': self.year_var.get(),
            'Program': self.program_entry.get().strip(),
            'College': self.college_entry.get().strip()
        }
        
        # Validate
        if not student_data['ID Number'] or not student_data['Name']:
            messagebox.showerror("Error", "ID Number and Name are required!")
            return
        
        # Call controller
        self.controller.add_student_from_dialog(student_data)
        self.dialog.destroy()
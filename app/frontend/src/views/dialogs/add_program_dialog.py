from pathlib import Path
import tkinter as tk
from tkinter import messagebox

class AddProgramDialog:
    def __init__(self, parent, controller):
        self.controller = controller
        self.result = None

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Program")
        self.dialog.geometry("400x500")
        self.dialog.configure(background="#F8ECD1")
        self.dialog.resizable(False, False)
        self.dialog.grab_set() 

        self.create_widgets()
        
        # Center the window
        self.dialog.transient(parent)
        self._center_window()

    def _center_window(self):
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (self.dialog.winfo_width() // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (self.dialog.winfo_height() // 2)
        self.dialog.geometry(f'+{x}+{y}')

    def create_widgets(self):
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
        form_frame = tk.Frame(self.dialog, padx=30, pady=20, bg="#F8ECD1")
        form_frame.pack(fill="both", expand=True)
        
        # Program Code
        tk.Label(form_frame, background="#F8ECD1", text="Program Code:", font=("Lato", 10)).grid(row=0, column=0, sticky="w", pady=10)
        self.id_entry = tk.Entry(form_frame, bg="#DEB6AB", font=("Lato", 10), width=30)
        self.id_entry.grid(row=0, column=1, pady=10)
        
        # Program Name
        tk.Label(form_frame, background="#F8ECD1", text="Program Name:", font=("Lato", 10)).grid(row=1, column=0, sticky="w", pady=10)
        self.name_entry = tk.Entry(form_frame,bg="#DEB6AB", font=("Lato", 10), width=30)
        self.name_entry.grid(row=1, column=1, pady=10)
        
        # College Code
        tk.Label(form_frame, background="#F8ECD1",  text="College Code:", font=("Lato", 10)).grid(row=4, column=0, sticky="w", pady=10)
        self.program_entry = tk.Entry(form_frame, bg="#DEB6AB", font=("Lato", 10), width=30)
        self.program_entry.grid(row=4, column=1, pady=10)
        
        # College
        tk.Label(form_frame, background="#F8ECD1",  text="College Name:", font=("Lato", 10)).grid(row=5, column=0, sticky="w", pady=10)
        self.college_entry = tk.Entry(form_frame, bg="#DEB6AB", font=("Lato", 10), width=30)
        self.college_entry.grid(row=5, column=1, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.dialog, bg="#F8ECD1",pady=20)
        button_frame.pack()
        
        # Save button
        save_btn = tk.Button(
            button_frame,
            text="Save",
            font=("Lato", 10, "bold"),
            background="#85586F",
            foreground="white",
            width=12,
            command=self.on_save,
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
    
    def on_save(self):
        # Collect form data
        program_data = {
            'Program Code': self.id_entry.get().strip(),
            'Program Name': self.name_entry.get().strip(),
            'College Code': self.program_entry.get().strip(),
            'College Name': self.college_entry.get().strip()
        }
        
        # Validate
        if not program_data['Program Code'] or not program_data['Program Name']:
            messagebox.showerror("Error", "ID Number and Name are required!")
            return
        
        # Call controller
        self.controller.add_program_from_dialog(program_data)
        self.dialog.destroy()
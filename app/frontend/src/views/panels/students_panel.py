from pathlib import Path
from pydoc import text
import sys
import tkinter as tk
import csv
from tkinter import CENTER, Button, Canvas, Frame, PhotoImage, Label, StringVar, ttk, Entry, messagebox

BASE_DIR = Path(__file__).resolve().parent
ASSETS_PATH = BASE_DIR.parent.parent.parent / "assets"
CONTROLLER_PATH = BASE_DIR.parent.parent.parent.parent / 'backend' / 'src' / 'Controller'

sys.path.insert(0, str(CONTROLLER_PATH))
from student_controller import StudentController

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class StudentPanel(Frame): 
    def __init__(self, parent, controller, user_role="user"):
        super().__init__(parent, bg="#F8ECD1") 
        self.controller = controller
        self.user_role = user_role
        self.student_controller = StudentController(self, user_role)
        self.sort_column = "Name"
        self.sort_reverse = False
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self,                        # ← self, not self.window
            width=1260, 
            height=680,
            bg="#F8ECD1",
            bd=0,
            highlightthickness=0
        )

        self.canvas.create_rectangle(0, 0, 1260, 85, fill="#85586F", outline="")
        self.canvas.create_rectangle(0, 85, 250, 680, fill="#DEB6AB", outline="")
        self.canvas.create_text(380, 120, text="Student Records", font=("Arial", 16), fill="Black")

        self.logo = PhotoImage(file=relative_to_assets("logo_wow.png"))
        self.logo_image = Label(self, image=self.logo, bg="#85586F")
        self.logo_image.place(x=10.0, y=20.0, width=200.0, height=60)

        self.student_button_image = PhotoImage(file=relative_to_assets("student_button.png"))
        self.student_button = Button(
            self,
            image=self.student_button_image,
            borderwidth=0, highlightthickness=0,
            command=lambda: self.controller.show_panel("student"),  # ← controller
            relief="flat", activebackground="#DEB6AB", cursor="hand2",
        )

        self.program_button_image = PhotoImage(file=relative_to_assets("program_button.png"))
        self.program_button = Button(
            self,
            image=self.program_button_image,
            borderwidth=0, highlightthickness=0,
            command=lambda: self.controller.show_panel("program"),  # ← controller
            relief="flat", activebackground="#DEB6AB", cursor="hand2",
        )

        self.college_button_image = PhotoImage(file=relative_to_assets("college_button.png"))
        self.college_button = Button(
            self,
            image=self.college_button_image,
            borderwidth=0, highlightthickness=0,
            command=lambda: self.controller.show_panel("college"),  # ← controller
            relief="flat", activebackground="#DEB6AB", cursor="hand2",
        )

        self.setting_button_image = PhotoImage(file=relative_to_assets("settings_button.png"))
        self.setting_button = Button(
            self,
            image=self.setting_button_image,
            borderwidth=0, highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat", activebackground="#DEB6AB", cursor="hand2",
        )

        self.search_bar_image = PhotoImage(file=relative_to_assets("TextBox.png"))
        self.search_bar = self.canvas.create_image(620.0, 125.0, image=self.search_bar_image)
        self.search_entry = Entry(
            self,
            bd=0, bg="#DEB6AB", fg="#000716",
            highlightthickness=0, font=("Inter", 11)
        )
        self.search_entry.bind("<Return>", lambda e: self.on_search())

        self.search_button_image = PhotoImage(file=relative_to_assets("search_button.png"))
        self.search_button = Button(
            self,
            image=self.search_button_image,
            borderwidth=0, highlightthickness=0,
            command=self.on_search,
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )

        # self.sort_button_image = PhotoImage(file=relative_to_assets("sort_button.png"))
        # self.sort_button = Button(
        #     self,
        #     image=self.sort_button_image,
        #     borderwidth=0, highlightthickness=0,
        #     command=lambda: print("Clicked"),
        #     relief="flat", activebackground="#F8ECD1", cursor="hand2",
        # )

        self.sort_variable = StringVar(value="Sort by")
        self.sort_dropdown = ttk.Combobox(
            self,
            textvariable=self.sort_variable,
            values=['ID Number', 'Name', 'Gender', 'Year Level', 'Program', 'College'],
            state='readonly',
            font=("Lato", 10),
            width=12
        )
        self.sort_dropdown.bind("<<ComboboxSelected>>", self.on_sort)

        self.add_button = Button(
            self,
            text="Add Student",
            font=("Lato", 10, "bold"),
            borderwidth=0, highlightthickness=0,
            background="#85586F",
            foreground="white",
            command=self.open_add_dialog,
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )

        self.edit_button = Button(
            self,
            text="Edit Student",
            font=("Lato", 10, "bold"),
            borderwidth=0, highlightthickness=0,
            background="#85586F",
            foreground="white",
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
            command=self.open_edit_dialog
        )
        
        self.delete_button = Button(
            self,
            text="Delete Student",
            font=("Lato", 10, "bold"),
            borderwidth=0, highlightthickness=0,
            background="#85586F",
            foreground="white",
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
            command=self.delete_selected_student
        )

        self.canvas.create_text(
            392, 175,
            text="Student",
            font=("Lato", 24),
            fill="#642D48",
            anchor="e")

        self.student_button.place(x=25.0, y=110.0, width=213.0, height=31)
        self.program_button.place(x=15.0, y=160.0, width=216, height=31)
        self.college_button.place(x=16.0, y=210.0, width=215, height=31)
        self.setting_button.place(x=18.0, y=630.0, width=215, height=31)
        self.search_entry.place(x=280.0, y=112.0, width=600, height=26.0)
        self.search_button.place(x=980.0, y=108.0, width=52, height=35.0)
        self.sort_dropdown.place(x=1038.0, y=108.0, width=101, height=35.0)
        self.add_button.place(x=450.0, y=165.0, width=90, height=30.0)
        self.edit_button.place(x=550.0, y=165.0, width=90, height=30.0)
        self.delete_button.place(x=650.0, y=165.0, width=100, height=30.0)


        self.canvas.pack(fill="x")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", bg="#A6738D", fg="#A6738D", fieldbackground="#D8A9C2")
        self.style.configure("Treeview.Heading", background="#884668", foreground="#D8A9C2", font=('Trebuchet MS', 10, 'bold'))

        self.tree = ttk.Treeview(self,
            columns=('ID Number', 'Name', 'Gender', 'Year Level', 'Program', 'College'),
            show='tree headings')

        self.tree.column("#0", width=40, minwidth=40, stretch=False)
        self.tree.column("ID Number", width=100, minwidth=100, stretch=False)
        self.tree.column("Name", width=200, minwidth=200, stretch=False)
        self.tree.column("Gender", width=105, minwidth=105, stretch=False)
        self.tree.column("Year Level", width=100, minwidth=100, stretch=False)
        self.tree.column("Program", width=200, minwidth=200, stretch=False)
        self.tree.column("College", width=200, minwidth=200, stretch=False)

        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading('ID Number', text='ID Number', anchor=CENTER)
        self.tree.heading('Name', text='Name')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Year Level', text='Year Level')
        self.tree.heading('Program', text='Program')
        self.tree.heading('College', text='College')

        self.tree.bind('<Button-1>', lambda e: 'break' if self.tree.identify_region(e.x, e.y) == 'separator' else None)
        self.tree.place(x=280.0, y=200.0, width=950, height=450.0)

        self.populate_students()
        self.setup_buttons(self.user_role)
    
    def populate_students(self, data=None):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.tree.tag_configure("odd", background="#DEB6AB", foreground="#000000")  
        self.tree.tag_configure("even", background="#AC7D88", foreground="#FFFFFF") 

        try:
            if data is None:
                csv_path = BASE_DIR.parent.parent.parent.parent / "backend" / "data" / "students.csv"
                with open(csv_path, newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    data = list(reader)

            for i, row in enumerate(data):       
                tag = "odd" if i % 2 == 0 else "even"
                self.tree.insert("", "end", text=str(i+1), values=(
                    row["ID Number"],
                    row["Name"],
                    row["Gender"],
                    row["Year Level"],
                    row["Program"],
                    row["College"]
                ), tags=(tag,))          
        except FileNotFoundError:
            print(f"CSV file not found at: {csv_path}")

    def open_add_dialog(self):
        dialog_path = Path(__file__).resolve().parent.parent / "dialogs"
        sys.path.insert(0, str(dialog_path))
        from add_student_dialog import AddStudentDialog
        AddStudentDialog(self, self.student_controller)

    def open_edit_dialog(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("No Selection", "Please select a student to edit.")
            return

        item = self.tree.item(selected[0])
        values = item['values'] 

        student_data = {
        'ID Number': str(values[0]),
        'Name': values[1],
        'Gender': values[2],
        'Year Level': str(values[3]),
        'Program': values[4],
        'College': values[5]
        }

        dialog_path = Path(__file__).resolve().parent.parent / "dialogs"
        sys.path.insert(0, str(dialog_path))
        from edit_student_dialog import UpdateStudentDialog
        UpdateStudentDialog(self, self.student_controller, student_data)

    def delete_selected_student(self):
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showwarning("No Selection", "Please select a student to delete.")
            return
        
        item = self.tree.item(selected[0])
        student_id = item['values'][0]

        self.student_controller.delete_student(str(student_id))

    def setup_buttons(self, user_role):
        if user_role != 'admin':
            self.delete_button.config(state="disabled")
            self.delete_button.configure(background="#A49A97")
            self.edit_button.config(state="disabled")
            self.edit_button.configure(background="#A49A97")
        else:
            self.delete_button.config(state="normal")
            self.edit_button.config(state="normal")

    def on_search(self):
        query = self.search_entry.get().strip()
        if query:
            self.student_controller.search_student(query)
        else:
            self.populate_students()

    def on_sort(self, event=None):
        column = self.sort_variable.get()
        if column == "Sort By":
            return
        
        if column == self.sort_column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = column
            self.sort_reverse = False
        
        self.student_controller.sort_student(self.sort_column, self.sort_reverse)

if __name__ == "__main__":
    from main_panel import MainPanel
    app = MainPanel(user_role="admin")
    app.show_panel("student")
    app.run()

    
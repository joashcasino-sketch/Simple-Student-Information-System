import csv
from pathlib import Path
import sys
import tkinter as tk
from tkinter import CENTER, Button, Canvas, Frame, PhotoImage, Label, ttk, Entry

BASE_DIR = Path(__file__).resolve().parent
ASSETS_PATH = BASE_DIR.parent.parent.parent / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CollegePanel(Frame): 
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F8ECD1") 
        self.controller = controller 
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

        self.search_button_image = PhotoImage(file=relative_to_assets("search_button.png"))
        self.search_button = Button(
            self,
            image=self.search_button_image,
            borderwidth=0, highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )

        self.sort_button_image = PhotoImage(file=relative_to_assets("sort_button.png"))
        self.sort_button = Button(
            self,
            image=self.sort_button_image,
            borderwidth=0, highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )

        self.add_button = Button(
            self,
            text="Add College",
            font=("Lato", 10, "bold"),
            borderwidth=0, highlightthickness=0,
            background="#85586F",
            foreground="white",
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )

        self.edit_button = Button(
            self,
            text="Edit College",
            font=("Lato", 10, "bold"),
            borderwidth=0, highlightthickness=0,
            background="#85586F",
            foreground="white",
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )
        
        self.delete_button = Button(
            self,
            text="Delete College",
            font=("Lato", 10, "bold"),
            borderwidth=0, highlightthickness=0,
            background="#85586F",
            foreground="white",
            relief="flat", activebackground="#F8ECD1", cursor="hand2",
        )

        self.canvas.create_text(
            390, 175,
            text="College",
            font=("Lato", 24),
            fill="#642D48", anchor="e")

        self.student_button.place(x=18.0, y=110.0, width=213.0, height=31)
        self.program_button.place(x=15.0, y=160.0, width=216, height=31)
        self.college_button.place(x=24.0, y=210.0, width=215, height=31)
        self.setting_button.place(x=18.0, y=630.0, width=215, height=31)
        self.search_entry.place(x=280.0, y=112.0, width=600, height=26.0)
        self.search_button.place(x=980.0, y=108.0, width=52, height=35.0)
        self.sort_button.place(x=1038.0, y=108.0, width=101, height=35.0)
        self.add_button.place(x=450.0, y=165.0, width=90, height=30.0)
        self.edit_button.place(x=550.0, y=165.0, width=90, height=30.0)
        self.delete_button.place(x=650.0, y=165.0, width=100, height=30.0)

        self.canvas.pack(fill="x")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", bg="#A6738D", fg="#A6738D", fieldbackground="#D8A9C2")
        self.style.configure("Treeview.Heading", background="#884668", foreground="#D8A9C2", font=('Trebuchet MS', 10, 'bold'))

        self.tree = ttk.Treeview(self,
            columns=('College Code', 'College Name'),
            show='tree headings')

        self.tree.column("#0", width=40, minwidth=40, stretch=False)
        self.tree.column("College Code", width=455, minwidth=100, stretch=False)
        self.tree.column("College Name", width=450, minwidth=200, stretch=False)

        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading('College Code', text='College Code', anchor=CENTER)
        self.tree.heading('College Name', text='College Name')

        self.tree.bind('<Button-1>', lambda e: 'break' if self.tree.identify_region(e.x, e.y) == 'separator' else None)
        self.tree.place(x=280.0, y=200.0, width=950, height=450.0)

        self.populate_college()

    def populate_college(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.tree.tag_configure("odd", background="#DEB6AB", foreground="#000000")   # black
        self.tree.tag_configure("even", background="#AC7D88", foreground="#FFFFFF")  # white
        try:
            csv_path = BASE_DIR.parent.parent.parent.parent / "backend" / "data" / "colleges.csv"
            with open(csv_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):        # ← enumerate for index
                    tag = "odd" if i % 2 == 0 else "even"
                    self.tree.insert("", "end", text=str(i+1), values=(
                        row["College Code"],
                        row["College Name"],
                    ), tags=(tag,))          
        except FileNotFoundError:
            print(f"CSV file not found at: {csv_path}")

if __name__ == "__main__":
    from main_panel import MainPanel
    app = MainPanel()
    app.show_panel("college")
    app.run()
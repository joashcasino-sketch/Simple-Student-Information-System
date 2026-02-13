from pathlib import Path

BASE_DIV = Path(__file__).resolve().parent
ASSETS_PATH = BASE_DIV.parent.parent.parent / "frontend" / "assets"

from tkinter import Button, Canvas, PhotoImage, Tk, Label, ttk, Entry

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class StudentPanel: # Using PascalCase for classes is a Python standard
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1260x680")
        self.window.resizable(False, False)
        self.window.title("Student Panel")
        self.window.configure(bg="#F8ECD1")
        self.setup_ui()

    def setup_ui(self):
        # Using pack or grid is usually easier than place for layouts

        self.canvas = Canvas(
            self.window, 
            width=1260, 
            height=680,
            bg="#F8ECD1",
            bd=0,
            highlightthickness=0
            )
        

        self.canvas.create_rectangle(
            0, 0,
            1260, 85,
            fill="#85586F",
            outline=""
        )

        self.canvas.create_rectangle(
            0, 85,
            250, 680,
            fill="#DEB6AB",
            outline=""
        )

        self.canvas.create_text(
            380, 120,
            text="Student Records",
            font=("Arial", 16),
            fill="Black"
        )

        self.logo = PhotoImage(file=relative_to_assets("logo_wow.png"))
        self.logo_image = Label(
            self.window,
            image=self.logo,
            bg="#85586F"
        )
        self.logo_image.place(x=10.0, y=20.0, width=200.0, height=60)

        self.student_button_image = PhotoImage(file=relative_to_assets("student_button.png"))
        self.student_button = Button(
            self.window,
            image=self.student_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat",
            activebackground="#DEB6AB",
            cursor="hand2",
        )

        self.program_button_image = PhotoImage(file=relative_to_assets("program_button.png"))
        self.program_button = Button(
            self.window,
            image=self.program_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat",
            activebackground="#DEB6AB",
            cursor="hand2",
        )

        self.college_button_image = PhotoImage(file=relative_to_assets("college_button.png"))
        self.college_button = Button(
            self.window,
            image=self.college_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat",
            activebackground="#DEB6AB",
            cursor="hand2",
        )

        self.setting_button_image = PhotoImage(file=relative_to_assets("settings_button.png"))
        self.setting_button = Button(
            self.window,
            image=self.setting_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat",
            activebackground="#DEB6AB",
            cursor="hand2",
        )

        self.search_bar_image = PhotoImage(file=relative_to_assets("TextBox.png"))
        self.search_bar = self.canvas.create_image(620.0, 125.0, image=self.search_bar_image)
        self.search_entry = Entry(
            self.window,
            bd=0,
            bg="#DEB6AB",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 11)
            )
    
        self.search_button_image = PhotoImage(file=relative_to_assets("search_button.png"))
        self.search_button = Button(
            self.window,
            image=self.search_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat",
            activebackground="#F8ECD1",
            cursor="hand2",
        )

        self.sort_button_image = PhotoImage(file=relative_to_assets("sort_button.png"))
        self.sort_button = Button(
            self.window,
            image=self.sort_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clicked"),
            relief="flat",
            activebackground="#F8ECD1",
            cursor="hand2",
        )

        self.student_button.place(x=18.0, y=110.0, width=213.0, height=31)
        self.program_button.place(x=18.0, y=160.0, width=216, height=31)
        self.college_button.place(x=18.0, y=210.0, width=215, height=31)
        self.setting_button.place(x=18.0, y=630.0, width=215, height=31)
        self.search_entry.place(x=280.0, y=112.0, width=600, height=26.0)
        self.search_button.place(x=980.0, y=108.0, width=52, height=35.0)
        self.sort_button.place(x=1038.0, y=108.0, width=101, height=35.0)



        self.canvas.pack(fill="x")

        # Create the Treeview (The CSV Display)
        self.tree = ttk.Treeview(self.window)
        self.tree.pack(expand=True, padx=20, pady=20)



    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = StudentPanel()
    app.run()
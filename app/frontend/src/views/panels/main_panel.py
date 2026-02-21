import sys
from pathlib import Path
import tkinter as tk

from students_panel import StudentPanel

BASE_DIR = Path(__file__).resolve().parent
ASSETS_PATH = BASE_DIR.parent.parent.parent / "assets"
CONTROLLER_PATH = BASE_DIR.parent.parent.parent.parent / 'backend' / 'src' / 'Controller'
sys.path.insert(0, str(CONTROLLER_PATH))

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainPanel:
    def __init__(self, user_role):
        self.user_role = user_role
        self.root = tk.Tk()
        self.root.geometry("1260x680")
        self.root.resizable(False, False)
        self.root.title("Student Information System")
        self.root.configure(bg="#F8ECD1")
        self.current_panel = None
        self.panels = {}

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.create_all_panels()
        self.show_panel("student")

    def create_all_panels(self):
        from students_panel import StudentPanel
        from programs_panel import ProgramPanel
        from colleges_panel import CollegePanel
        from student_controller import StudentController
        from program_controller import ProgramController
        from college_controller import CollegeController

        panels_config = [
        (StudentPanel, None, "student", {"user_role": self.user_role}),  # ← None, handled internally
        (ProgramPanel, ProgramController, "program", {}),
        (CollegePanel, CollegeController, "college", {})
        ]


        for PanelClass, ControllerClass, name, kwargs in panels_config:
            frame = PanelClass(self.container, self, **kwargs)
            if ControllerClass:
                ControllerClass(views=frame)
            self.panels[name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

    def show_panel(self, name):
        panel = self.panels[name]
        panel.lift()
        self.current_panel = panel


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainPanel(user_role="admin")
    app.run()
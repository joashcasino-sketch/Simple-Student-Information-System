from pathlib import Path
import tkinter as tk

BASE_DIV = Path(__file__).resolve().parent
ASSETS_PATH = BASE_DIV.parent.parent.parent / "frontend" / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1260x680")
        self.resizable(False, False)
        self.title("Student Information System")
        self.configure(bg="#F8ECD1")
        self.current_panel = None
        self.panels = {}

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.create_all_panels()
        self.show_panel("student")

    def create_all_panels(self):
        from students_panel import StudentPanel
        from programs_panel import ProgramPanel
        from colleges_panel import CollegePanel

        for PanelClass, name in [
            (StudentPanel, "student"),
            (ProgramPanel, "program"),
            (CollegePanel, "college")
        ]:
            frame = PanelClass(self.container, self)
            self.panels[name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

    def show_panel(self, name):
        panel = self.panels[name]
        if self.current_panel and self.current_panel != panel:
            self._animate_switch(self.current_panel, panel)
        else:
            panel.lift()
            self.current_panel = panel

    def _animate_switch(self, old_panel, new_panel, step=0):
        total_steps = 10
        width = self.winfo_width()

        if step == 0:
            new_panel.place(x=width, y=0, relwidth=1, relheight=1)
            new_panel.lift()

        if step <= total_steps:
            offset = int(width * (1 - step / total_steps))
            new_panel.place(x=offset, y=0, relwidth=1, relheight=1)
            old_panel.place(x=-int(width * step / total_steps), y=0, relwidth=1, relheight=1)
            self.after(16, lambda: self._animate_switch(old_panel, new_panel, step + 1))
        else:
            new_panel.place(x=0, y=0, relwidth=1, relheight=1)
            old_panel.place(x=0, y=0, relwidth=1, relheight=1)
            old_panel.lower()
            self.current_panel = new_panel

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MainPanel()
    app.run()
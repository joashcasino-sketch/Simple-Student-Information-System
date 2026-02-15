from pathlib import Path
from tkinter import Button, Canvas, Tk

BASE_DIV = Path(__file__).resolve().parent
from main_panel import MainPanel

class StudentPanel(MainPanel):
    def __init__(self):
        super().__init__()
        
    def setup_ui(self):
        super().setup_ui() 
    
        self.canvas.create_text(
        395, 170,
        text="Students",
        font=("Arial", 24),
        fill="Black",
        anchor="e"
        )
        self.program_button = Button(
            self.window,
            image=self.program_button_image,
            borderwidth=0,
            highlightthickness=0,
            command= self.open_program,
            relief="flat",
            activebackground="#DEB6AB",
            cursor="hand2",
        )
        
    def open_program(self):
        from programs_panel import ProgramPanel
        self.switch_to_panel(ProgramPanel)
    
    def run(self):
        return super().run()
    
def main():
    app = StudentPanel()
    app.run()

if __name__ == "__main__":
    main()
        



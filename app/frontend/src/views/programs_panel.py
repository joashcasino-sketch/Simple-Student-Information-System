from pathlib import Path
from tkinter import Tk

BASE_DIV = Path(__file__).resolve().parent
from main_panel import MainPanel

class ProgramPanel(MainPanel):
    def __init__(self):
        super().__init__()
        
    def setup_ui(self):
        super().setup_ui()
        self.canvas.create_text(
            405,170,
            text="Programs",
            font=("Arial", 24),
            fill="black",
            anchor="e"
        )
    
    def run(self):
        return super().run()
    
def main():
    app = ProgramPanel()
    app.run()

if __name__ == "__main__":
    main()
        



from pathlib import Path
from tkinter import Tk

BASE_DIV = Path(__file__).resolve().parent
from main_panel import MainPanel

class StudentPanel(MainPanel):
    def __init__(self):
        super().__init__()
        
    def setup_ui(self):

        return super().setup_ui()
    
    def run(self):
        return super().run()
    
def main():
    app = StudentPanel()
    app.run()

if __name__ == "__main__":
    main()
        



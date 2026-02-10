import tkinter as tk

class Test:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1260x680")
        self.setup_ui()
    
    def setup_ui(self):
        # Add your widgets here
        label = tk.Label(self.window, text="Test Window")
        label.pack()
    
    def run(self):  # ✅ Has 'self'
        self.window.mainloop()

def main():
    app = Test()
    app.run()

if __name__ == "__main__":
    main()
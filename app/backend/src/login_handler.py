import csv
import sys
from pathlib import Path
from tkinter import messagebox


BASE_DIR = Path(__file__).resolve().parent
frontend_src_path = BASE_DIR.parent.parent / 'frontend' / 'src'
sys.path.insert(0, str(frontend_src_path))

from test import Test

USER_CSV = BASE_DIR.parent / 'data' / 'users.csv'

with open(USER_CSV, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line)

class Login_Logic:

    def __init__(self, csv_path=USER_CSV):
        self.csv_path = csv_path
        self.setup_csv()

    def setup_csv(self):
        Path(self.csv_path).parent.mkdir(parents=True, exist_ok=True)

        if not Path(self.csv_path).exists():
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['username', 'password'])
    def check_user(self, username, password):
        with open(self.csv_path, mode='r') as file:
            reader = csv.DictReader(file)

            for line in reader:
                if line['username'] == username and line['password'] == password:
                    return True
            return False
    
    def register_user(self, username, password):
        with open(self.csv_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        return True

    
def handle_sign_in(username_entry, password_entry, login_window):
    username = username_entry.get().strip()
    password = password_entry.get()

    logic = Login_Logic()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return

    isValid = logic.check_user(username, password)

    if isValid is True:
        messagebox.showinfo("Success", "Login Success")
        login_window.destroy()
        run = Test()
        run.run()
    else:
        messagebox.showerror("Error", "Invalid")
        password_entry.delete(0, 'end')
    
def handle_sign_up(username_entry, password_entry):
    username = username_entry.get().strip()
    password = password_entry.get()

    logic = Login_Logic()

    register = logic.register_user(username, password)

    if register:
        messagebox.showinfo("Success", "You are now Registered")
    else:
        messagebox.showerror("Error", "Invalid")
        

        
       
    

    
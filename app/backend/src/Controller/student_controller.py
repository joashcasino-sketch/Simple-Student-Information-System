from email import message
import sys
from pathlib import Path
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent
student_view_path = BASE_DIR.parent.parent.parent / 'frontend' / 'src' / 'views' / 'panels'
student_model_path = BASE_DIR.parent / 'Model' 
sys.path.insert(0, str(student_view_path))
sys.path.insert(0, str(student_model_path))

from student_model import StudentModel

class StudentController:
    def __init__(self, views, user_role):
        self.model = StudentModel()
        self.views = views
        self.user_role = user_role

    def add_student_from_dialog(self, student_data):
        success = self.model.add_student(student_data)

        if success:
            messagebox.showinfo("Success", "Student Added Successfully!")
            self.views.populate_students()
        else:
            messagebox.showerror("Error", "Student ID Already Exist!")
        return success
    
    def update_student(self):
        pass

    def delete_student(self, student_id):
        if self.user_role != 'admin':
            messagebox.showerror("Access Denied!", "You don't have permission to delete user!")
            return
        
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student {student_id}?")
        if not confirm:
            return
        
        success = self.model.delete_student(student_id)
        if success:
            messagebox.showinfo("Success", "Student deleted successfully")
            self.views.populate_students()

        else:
            messagebox.showerror("Error", "Student not found.")

    def search_student(self):
        pass

    def sort_student(self):
        pass
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
    def __init__(self, views):
        self.model = StudentModel()
        self.views = views

    def add_student_from_dialog(self, student_data):
        success = self.model.add_student(student_data)

        if success:
            messagebox.showinfo("Success", "Student Added Successfully!")
            self.views.populate_students()
        else:
            messagebox.showerror("Error", "Student ID Already Exist!")
        return success
    
    def add_student(self):
        data = self.views.get_form_data()
        success = self.model.add_student(data)
        self.views.display_result(success)

    def update_student(self):
        pass

    def delete_student(self):
        pass

    def search_student(self):
        pass

    def sort_student(self):
        pass
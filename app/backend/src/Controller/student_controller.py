import sys
from pathlib import Path

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